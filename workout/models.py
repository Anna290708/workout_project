from django.db import models
from django.conf import settings

# Constants for difficulty levels and categories
DIFFICULTY_LEVELS = (
    ('easy', 'Easy'),
    ('medium', 'Medium'),
    ('hard', 'Hard'),
)

CATEGORIES = (
    ('arms', 'Arms'),
    ('legs', 'Legs'),
    ('cardio', 'Cardio'),
    ('pilates', 'Pilates'), 
    ('yoga', 'Yoga')
)

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORIES)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_LEVELS)
    duration = models.IntegerField(help_text="Duration in seconds (e.g., 30)")
    description = models.TextField()
    image = models.ImageField(upload_to='exercise_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.get_category_display()} - {self.get_difficulty_display()})"


class WorkoutPlan(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    exercises = models.ManyToManyField('Exercise')
    duration = models.IntegerField(help_text="Total workout duration in minutes")
    difficulty = models.CharField(max_length=10, choices=[('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard')])
    category = models.CharField(max_length=20, choices=CATEGORIES)
    date_created = models.DateTimeField(auto_now_add=True)
    ordering = ['date_created']

    def __str__(self):
        if self.date_created:
            return f"Workout on {self.date_created.date()}"
        else:
            return "Workout (not saved yet)"


class WorkoutVideo(models.Model):
    DIFFICULTY_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]

    title = models.CharField(max_length=100)
    video_url = models.URLField()
    type = models.CharField(max_length=50)  # e.g. "Cardio", "Yoga"
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES)

    def __str__(self):
        return self.title
    @property
    def get_embed_url(self):
        """
        Convert YouTube video URLs to the embeddable iframe URL format.
        """
        url = self.video_url

        if "youtube.com/watch?v=" in url:
            video_id = url.split("watch?v=")[-1].split("&")[0]  # strip extra params
            return f"https://www.youtube.com/embed/{video_id}"
        elif "youtu.be/" in url:
            video_id = url.split("youtu.be/")[-1].split("?")[0]
            return f"https://www.youtube.com/embed/{video_id}"
        else:
            return url