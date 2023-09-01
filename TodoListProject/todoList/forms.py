
from django import forms
from todoList.models import TaskModel


class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields =['tasktitle','taskDescription']
