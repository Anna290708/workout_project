from django import forms
from .models import CATEGORIES, DIFFICULTY_LEVELS
from .models import WorkoutVideo


class WorkoutFilterForm(forms.Form):
    search = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Search videos...'}))
    type = forms.CharField(required=False)
    difficulty = forms.ChoiceField(
        required=False,
        choices=[('', 'Any Difficulty')] + WorkoutVideo.DIFFICULTY_CHOICES,
    )

class WorkoutForm(forms.Form):
    duration = forms.IntegerField(min_value=1, label="Duration (minutes)")
    category = forms.ChoiceField(choices=CATEGORIES)
    difficulty = forms.ChoiceField(choices=DIFFICULTY_LEVELS)
