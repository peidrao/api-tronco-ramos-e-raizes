from rest_framework import  serializers
from .models import Audio

class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields = ('id', 'file', 'name', 'created_at', 'updated_at')
        #fields = ('id', 'url', 'file', 'name', 'created_at', 'updated_at') 
    
   
