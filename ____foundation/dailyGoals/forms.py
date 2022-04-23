from django import forms

from .models import DailyGoal

# forms below

class DailyGoalForm(forms.ModelForm):
    class Meta:
        model = DailyGoal
        fields = "__all__"


    widgets = {
     # 'name': forms.CharField(attrs={'class': 'works'})
    }
