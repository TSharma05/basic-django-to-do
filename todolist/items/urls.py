from django.urls import path
from .views import *

app_name = 'items'
urlpatterns = [
    path('items/', index, name='index'),
    path('all', all_tasks, name='all_tasks'),
    path('<int:task_id>', task_view, name='task_view'),
    path('edit/<int:task_id>', task_update, name='task_update'),
    path('delete/<int:task_id>', task_delete, name='task_delete'),
]