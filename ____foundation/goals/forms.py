from django.forms import ModelForm
from django import forms

from .models import Goal

# forms below


class DateInputChange(forms.DateInput):
    input_type = 'date'
    # is_hidden = False
    # forms.use_request_attribute = False

class SlideInputChange(forms.NumberInput):
    input_type = 'range'
    input_min="1"
    input_max="3"
    # step=3

class GoalForm(ModelForm):
    class Meta:
        model = Goal
        fields = ['name', 'priority', 'description', 'deadline']

        widgets = {
            # 'name': forms.TextInput(attrs={'class': 'test'})
            # 'priority': SlideInputChange(attrs={'class': 'test4'}),
            'priority': SlideInputChange(attrs={'class': 'test4', 'min': 1, 'max': 3,}),
            'deadline': DateInputChange()
        }

        # prority = range
