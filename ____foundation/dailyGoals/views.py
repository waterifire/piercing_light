from django.shortcuts import render, redirect

from .models import DailyGoal
from .forms import DailyGoalForm

# Create your views here.

def dg_home(request):
    goals = DailyGoal.objects.all()
    form = DailyGoalForm()

    if request.method == "POST":
        form = DailyGoalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dg_home')
    context = {'goals': goals, 'form': form}
    return render(request, 'dg/dg_home.html', context)

def dg_add(request):
    form = DailyGoalForm()

    if request.method == "POST":
        form = DailyGoalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dg_home')
    context = {'form': form}

    return render(request, 'dg/dg_add.html', context)
