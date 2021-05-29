from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Dailygoal
from .filters import DailygoalFilter
from .forms import CreateDailygoalForm, EditDailygoalForm


@login_required
def daily_goals_index(request):
    # daily_goals = Dailygoal.objects.all()
    daily_goals = Dailygoal.objects.filter(created_by=request.user)
    daily_goals_filter = DailygoalFilter(request.GET, queryset=daily_goals)
    context = {'daily_goals_filter': daily_goals_filter}
    return render(request, 'goals/daily_goals/daily_goals_index.html', context)
    # don't forgot the infinit scroll



@login_required
def daily_goal_details(request, pk):
    daily_goal = get_object_or_404(Dailygoal, pk=pk, created_by=request.user)
    context = {'daily_goal': daily_goal}
    return render(request, 'goals/daily_goals/daily_goal_details.html', context)


@login_required
def create_daily_goal(request):
    form = CreateDailygoalForm()

    if request.method == 'POST':
        form = CreateDailygoalForm(request.POST)
        if form.is_valid():
            form.instance.created_by = request.user
            form.save()
            messages.success(request, 'your daily goals has been created')
            return redirect("goals:daily_goals_list")
        else:
            messages.error(request, 'error when creating daily goals')

    context = {'form': form}
    return render(request, 'goals/daily_goals/create_daily_goal.html', context)


@login_required
def edit_daily_goal(request, pk):

    daily_goal = get_object_or_404(Dailygoal, pk=pk, created_by=request.user)
    form = EditDailygoalForm(instance=daily_goal)

    if request.user != daily_goal.created_by:
        return HttpResposen("you don't have permission")

    if request.method == 'POST':
        form = EditDailygoalForm(data=request.POST, instance=daily_goal)
        if form.is_valid():
            form.save()
            messages.success(request, 'your daily goals has been edited')
            return redirect("goals:daily_goals_list")
        else:
            messages.error(request, 'error when editing daily goals')

    context = {'form': form}
    return render(request, 'goals/daily_goals/edit_daily_goal.html', context)


@login_required
def delete_daily_goal(request, pk):

    daily_goal = get_object_or_404(Dailygoal, pk=pk, created_by=request.user)

    if request.user != daily_goal.created_by:
        return HttpResposen("you don't have permission")

    if request.method == 'POST':
        daily_goal.delete()
        messages.error(request, 'your daily goals has been deleted')
        return redirect("goals:daily_goals_list")

    context = {'daily_goal': daily_goal}
    return render(request, 'goals/daily_goals/delete_daily_goal.html', context)



