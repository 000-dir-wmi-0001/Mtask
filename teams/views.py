from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Team, TaskAssignment
from .forms import TeamForm, TaskAssignmentForm
from tasks.models import Task

@login_required
def create_team(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            team = form.save()
            team.members.add(request.user)
            return redirect('team_list')
    else:
        form = TeamForm()
    return render(request, 'team_form.html', {'form': form})

@login_required
def team_list(request):
    teams = Team.objects.filter(members=request.user)
    return render(request, 'team_list.html', {'teams': teams})

@login_required
def assign_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskAssignmentForm(request.POST)
        if form.is_valid():
            task_assignment = form.save(commit=False)
            task_assignment.task = task
            task_assignment.save()
            return redirect('task_list')
    else:
        form = TaskAssignmentForm(initial={'task': task})
    users = User.objects.all()
    return render(request, 'assign_task.html', {'task': task, 'users': users, 'form': form})
