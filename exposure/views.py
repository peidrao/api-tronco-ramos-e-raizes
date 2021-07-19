from django.shortcuts import render

# Create your views here.
from exposure.models import *
from exposure.serializers import *
from rest_framework import viewsets



class ExposureViewSet(viewsets.ModelViewSet):
    serializer_class = ExposureSerializer
    queryset = Exposure.objects.all()



class GeoViewSet(viewsets.ModelViewSet):
    