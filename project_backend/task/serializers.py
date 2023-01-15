from rest_framework import serializers

from project_backend import models 

class AddTaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Task
        fields = ['id','taskName','taskDesc','taskLocation','taskStartDate','taskStopDate','taskPrice','taskStatus','taskCarriedBy']

class UpdateTaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Task
        fields = ['taskName','taskDesc','taskLocation','taskStartDate','taskStopDate','taskPrice']
        
class UpdateProxyTaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Task
        fields = ['taskStatus']
        
class TaskListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Task
        fields = ['id','taskName','taskDesc','taskLocation','taskStartDate','taskStopDate','taskPrice','taskStatus','taskAssignedby','taskCarriedBy']