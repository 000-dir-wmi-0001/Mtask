from django.db import models
from django.contrib.auth.models import User
from tasks.models import Task

class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User)
    def __str__(self):
        return self.name

class TaskAssignment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    assigned_user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.assigned_user.username} assigned to {self.task.title}"
