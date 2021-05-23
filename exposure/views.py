from exposure.models import Exposure
from exposure.serializers import ExposureSerializer
from rest_framework import viewsets
from rest_framework.response import Response



class ExposureViewSet(viewsets.ModelViewSet):
    serializer_class = ExposureSerializer
    queryset = Exposure.objects.all()