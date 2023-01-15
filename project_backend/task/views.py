from django.http import Http404

from rest_framework import generics, views
from rest_framework import status

from project_backend import models
from project_backend.task import serializers
from project_backend import utils
from project_backend.permissions import IsActiveVerifiedAuthenticated
from project_backend.task.utils import (IsPrincipalTask,IsProxyTask)

class PrincipalAddTask(generics.ListCreateAPIView):
    '''
    A class that allow for saving and listing all task
    added by a principal.
    Allowed HTTP methods are POST & GET
    '''
    permission_classes = [IsActiveVerifiedAuthenticated,IsPrincipalTask]
    queryset = models.Task.objects.all()
    serializer_class = serializers.AddTaskSerializer
    
    def perform_create(self, serializer):
        serializer.save(taskAssignedby=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(taskAssignedby=self.request.user)

class PrincipalUpdateTask(generics.GenericAPIView):
    '''
    A class that allow for retrieving and updating task
    added by a principal.
    Allowed method is PUT
    '''
    permission_classes = [IsActiveVerifiedAuthenticated,IsPrincipalTask]
    serializer_class = serializers.UpdateTaskSerializer

    def get_object(self, id):
        try:
            return models.Task.objects.get(id=id)
        except models.Task.DoesNotExist:
            raise Http404
        
    def put(self, request, id, format=None):
        task = self.get_object(id)
        
        if task.taskStatus in ['Started','Completed']:
            return utils.CustomResponse.Failure("Task has been Started or Completed")
        
        serializer = self.serializer_class(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return utils.CustomResponse.Success("Task Updated Successfully", status=status.HTTP_200_OK)
        
        return utils.CustomResponse.Failure(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProxyTaskHistory(generics.ListAPIView):
    '''
    A class that allow for listing of all task assigned to proxy user.
    Allowed method is GET   
    '''
    permission_classes = [IsActiveVerifiedAuthenticated,IsProxyTask]

    queryset = models.Task.objects.all()
    serializer_class = serializers.AddTaskSerializer
    
    def get_queryset(self):
        return self.queryset.filter(taskCarriedBy=self.request.user)
    
class UpdateProxyTask(generics.RetrieveUpdateAPIView):
    '''
    A class that allow for updating of all task been carried out by proxy user.
    Allowed method is PUT   
    '''
    queryset = models.Task.objects.all()
    serializer_class = serializers.UpdateProxyTaskSerializer
    lookup_field = 'pk'
    
    def perform_update(self, serializer):
        instance = serializer.save()
        # send_email_confirmation(user=self.request.user, modified=instance)

class TaskList(generics.ListAPIView):
    """
    A view for listing all task queryset.
    """
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskListSerializer
