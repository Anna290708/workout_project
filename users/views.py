from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .serializers import RegisterSerializer, LoginSerializer, ProfileSerializer, WorkoutHistorySerializer
from workout.models import *

class RegisterPageView(View):
    def get(self, request):
        serializer = RegisterSerializer()
        return render(request, 'register.html', {'form': serializer})

    def post(self, request):
        serializer = RegisterSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return redirect('login')  # redirect to login after registration success
        return render(request, 'register.html', {'form': serializer})

class LoginPageView(View):
    def get(self, request):
        serializer = LoginSerializer()
        return render(request, 'login.html', {'form': serializer})

    def post(self, request):
        serializer = LoginSerializer(data=request.POST)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)
            return redirect('profile')  
        return render(request, 'login.html', {'form': serializer})

class LogoutView(View):
    def post(self, request):
        logout(request)
        return redirect('login')

class ProfilePageView(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request):
        serializer = ProfileSerializer(request.user)
        
        # Fetch workout plans for this user, newest first
        workouts = WorkoutPlan.objects.filter(user=request.user).order_by('-date_created')

        context = {
            'user': serializer.data,
            'workouts': workouts,  # pass queryset directly to template
        }
        return render(request, 'profile.html', context)

class HistoryPageView(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request):
        # Get all workout plans for the user, newest first
        workout_plans = WorkoutPlan.objects.filter(user=request.user).order_by('-date_created')

        # Pass workout_plans to template; you can display plan details and exercises inside them
        return render(request, 'history.html', {'workout_plans': workout_plans})
