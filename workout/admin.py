from django.contrib import admin
from .models import *

# Registering Exercise model
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'difficulty', 'duration', 'description', 'image')
    list_filter = ('category', 'difficulty')
    search_fields = ('name', 'description')
    ordering = ('category', 'difficulty')


@admin.register(WorkoutPlan)
class WorkoutPlanAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_created', 'duration')
    list_filter = ('date_created', 'user')
    search_fields = ('user__username',)
    ordering = ['date_created']
    
# Register the models with custom admin options
admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(WorkoutVideo)

