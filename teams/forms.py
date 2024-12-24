from django import forms
from .models import Team, TaskAssignment
from tasks.models import Task

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'members']

class TaskAssignmentForm(forms.ModelForm):
    class Meta:
        model = TaskAssignment
        fields = ['task', 'assigned_user']
