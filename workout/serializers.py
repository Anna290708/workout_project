
from rest_framework import serializers
from .models import Exercise, WorkoutPlan

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'

class WorkoutPlanSerializer(serializers.ModelSerializer):
    exercises = ExerciseSerializer(many=True, read_only=True)
    
    class Meta:
        model = WorkoutPlan
        fields = ('id', 'user', 'exercises', 'duration', 'difficulty', 'category', 'date_created')