from django.shortcuts import render, redirect
from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import *
from quotes.models import Quote
from .serializers import ExerciseSerializer, WorkoutPlanSerializer
from quotes.serializers import QuoteSerializer
import random
from rest_framework.views import APIView
from .form import *
from django.contrib.auth.decorators import login_required
from .utils import search_youtube_videos

@login_required
def generate_workout_view(request):
    workout_plan = None  
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            workout_plan = WorkoutPlan.objects.create(
                user=request.user,
                duration=form.cleaned_data['duration'],
                difficulty=form.cleaned_data['difficulty'],
                category=form.cleaned_data['category']
            )
            exercises = Exercise.objects.filter(
                category=form.cleaned_data['category'],
                difficulty=form.cleaned_data['difficulty']
            )
            workout_plan.exercises.set(exercises)
            
            
            workout_plan.save()
            return render(request, 'generate_workout.html', {'form': form, 'workout_plan': workout_plan})
    else:
        form = WorkoutForm()
    return render(request, 'generate_workout.html', {'form': form})

class GenerateWorkoutPlanView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        duration = int(request.data.get('duration')) * 60 
        category = request.data.get('category')
        difficulty = request.data.get('difficulty')

        exercises = list(Exercise.objects.filter(
            category=category,
            difficulty=difficulty
        ).order_by('?'))  

        selected_exercises = []
        total_duration = 0

        for exercise in exercises:
            if total_duration + exercise.duration <= duration:
                selected_exercises.append(exercise)
                total_duration += exercise.duration
            if total_duration >= duration:
                break

        plan = WorkoutPlan.objects.create(
            user=request.user,
            duration=duration // 60,  
            difficulty=difficulty,
            category=category
        )
        plan.exercises.set(selected_exercises)

        quote = random.choice(Quote.objects.all())
        return Response({
            'plan': WorkoutPlanSerializer(plan).data,
            'quote': QuoteSerializer(quote).data
        })


class WorkoutHistoryView(generics.ListAPIView):
    serializer_class = WorkoutPlanSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return WorkoutPlan.objects.filter(user=self.request.user).order_by('-date_created')
    

def home_view(request):
    return render(request, 'home.html')


def workout_videos(request):
    form = WorkoutFilterForm(request.GET or None)
    videos = WorkoutVideo.objects.all()
    youtube_results = []

    if form.is_valid():
        search = form.cleaned_data.get('search')
        type_filter = form.cleaned_data.get('type')
        difficulty = form.cleaned_data.get('difficulty')

        if search:
            youtube_results = search_youtube_videos(search, max_results=12)
            videos = videos.filter(title__icontains=search)
        if type_filter:
            videos = videos.filter(type__icontains=type_filter)
        if difficulty:
            videos = videos.filter(difficulty=difficulty)

    return render(request, 'workout_videos.html', {
        'videos': videos,
        'youtube_videos': youtube_results,
        'form': form,
    })