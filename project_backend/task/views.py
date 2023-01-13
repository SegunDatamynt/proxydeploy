from rest_framework import generics, views
from rest_framework import status

from project_backend import models
from project_backend.task import serializers 

class AddTask(generics.ListCreateAPIView):
    pass 