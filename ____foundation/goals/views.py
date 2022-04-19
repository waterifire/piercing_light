from django.shortcuts import render, redirect

from .models import Goal
from .forms import GoalForm

# Create your views here.

def goals_home(request):
    testing = "test"
    goals = Goal.objects.all()


    context = {'goals': goals, 'testing': testing}
    return render(request, 'goals/goals_home.html', context)

def goals_add(request):
    page = 'add'
    form = GoalForm()

    if request.method == "POST":
        form = GoalForm(request.POST)

        if form.is_valid():
            goal_form = form.save(commit=False)
            goal_form.user = request.user
            goal_form.save()
            return redirect('goals_home')

    context = {'page': page,'form': form}
    return render(request, 'goals/goals_add.html', context)

def goals_edit(request, pk):
    goal = Goal.objects.get(id=pk)
    page = 'edit'
    form = GoalForm(instance=goal)

    if request.method == "POST":
        form = GoalForm(request.POST, instance=goal)
        if form.is_valid():
            form.save()
            return redirect('goals_home')

    context = {'page': page, 'goal': goal, 'form': form,}
    return render(request, 'goals/goals_add.html', context)
