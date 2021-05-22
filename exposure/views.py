from exposure.serializers import TaskSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import viewsets
from .models import Task


class ExposureViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    
    
