from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=50, choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')])
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)
    assigned_to = models.ManyToManyField(User, related_name='assigned_tasks', blank=True)
    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Comment by {self.user.username} on {self.task.title}"
