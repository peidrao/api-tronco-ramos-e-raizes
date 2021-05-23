from exposure.models import Exposure
from rest_framework import serializers

class ExposureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exposure
        fields = "__all__" 
