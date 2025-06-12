from django.urls import path, include
from .views import *
from . import views


urlpatterns = [
 
    path('generate/', GenerateWorkoutPlanView.as_view(), name='generate-workout'),
    path('history/', WorkoutHistoryView.as_view(), name='workout-history'),
    path('', home_view, name='home'),
    path('generate-form/', generate_workout_view, name='generate-form'),
    path('videos/', views.workout_videos, name='videos'),


]