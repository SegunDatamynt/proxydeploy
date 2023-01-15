from django.urls import path
from project_backend.task import views 

urlpatterns = [
    path('principal/add-task/', views.PrincipalAddTask.as_view(), name='principal-add-task'),
    path('principal/update-task/<int:id>/', views.PrincipalUpdateTask.as_view(), name='principal-update-task'),
    path('proxy/history/', views.ProxyTaskHistory.as_view(), name='proxy-task-history'),
    path('proxy/update-task/<int:pk>/', views.UpdateProxyTask.as_view(), name='proxy-update-task'),
    path('tasklist/', views.TaskList.as_view(), name='task-list')
]