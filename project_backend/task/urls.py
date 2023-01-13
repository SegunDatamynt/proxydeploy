from django.urls import path
from project_backend.task import views 

urlpatterns = [
    path('add-task/', views.AddTask.as_view(), name='add-task')
]