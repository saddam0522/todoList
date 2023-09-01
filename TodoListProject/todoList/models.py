from django.db import models

# Create your models here.


class TaskModel(models.Model):
    task_id = models.IntegerField(primary_key=True)
    tasktitle = models.CharField(max_length=50)
    taskDescription = models.TextField()
    is_completed = models.BooleanField(default=False)
    