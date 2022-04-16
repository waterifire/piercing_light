from django.forms import ModelForm

from .models import Goal

# forms below

class GoalForm(ModelForm):
    class Meta:
        model = Goal
        fields = ['name', 'priority', 'description', 'deadline']
        
