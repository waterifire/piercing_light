from django.shortcuts import render, redirect

from .models import Goal

# Create your views here.

def goals_home(request):
    goals = Goal.objects.all()
    context = {'goals': goals}
    return render(request, 'goals/goals_home.html', context)

def goals_add(request):
    context = {}
    return render(request, 'goals/goals_add.html', context)
