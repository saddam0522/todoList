from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="homepage"),
    path('show_task/',views.show_task, name="show_task"),
    path('edit_task/<int:id>',views.edit_task,name="edit_task"),
    path('delete_task/<int:id>',views.delete_task,name="delete_task"),
    path('complete_task/<int:id>',views.complete_task,name="complete_task"),
    path('completed_task/',views.completed_tasks,name="completed_task"),
    
]
