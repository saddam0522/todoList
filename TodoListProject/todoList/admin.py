from django.contrib import admin
from todoList.models import TaskModel

# Register your models here.

class TaskModelAdmin(admin.ModelAdmin):
    list_display = ('task_id','tasktitle','taskDescription','is_completed')

admin.site.register(TaskModel,TaskModelAdmin)