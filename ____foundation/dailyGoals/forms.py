from django import forms

from .models import DailyGoal, Note

# forms below

class DailyGoalForm(forms.ModelForm):
    class Meta:
        model = DailyGoal
        fields = "__all__"


        widgets = {
         'name': forms.TextInput(attrs={'class': 'goal-edit'})
        }

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = "__all__"
