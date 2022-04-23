from django.shortcuts import render, redirect

from .models import DailyGoal
from .forms import DailyGoalForm

# Create your views here.
# //TODO: Make all user inputs lowercase

def dg_home(request):
    goals = DailyGoal.objects.all()
    form = DailyGoalForm()

    # if request.method == "POST":
    #     form = DailyGoalForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('dg_home')


    if request.method == "POST":
        for goal in goals:
            if goal.name in request.POST:
                # form.DailyGoalForm(request.POST, instance=goal)
                # if form.is_valid():
                #     form.save()
                # //TODO: can we do this a better, more secure, less error way? I don't think it is the best
                goal.name = request.POST["name"].lower()
                goal.save()
                # return redirect('dg_home')
            if request.POST.get(f"remove_{goal.name}"):
                goal.delete()
                return redirect('dg_home')

    context = {'goals': goals, 'form': form}
    return render(request, 'dg/dg_home.html', context)


def dg_add(request):
    goals = DailyGoal.objects.all()
    # print(goals)

    # for goal in goals:
    #     print(goal)

    form = DailyGoalForm()

    if request.method == "POST":
        form = DailyGoalForm(request.POST)
        # print(request.POST)
        if form.is_valid():
            added_goal = form.save(commit=False)
            added_goal.name = added_goal.name.lower()
            added_goal.save()
            return redirect('dg_home')
    context = {'form': form}

    return render(request, 'dg/dg_add.html', context)


def dn_add(request):

    context = {}
    return render(request, 'dg/dn_add.html', context)
