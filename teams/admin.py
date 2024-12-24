from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Team, TaskAssignment

admin.site.register(Team)
admin.site.register(TaskAssignment)
