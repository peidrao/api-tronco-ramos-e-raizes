import os
from rest_framework import  serializers
from .models import Document

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('id', 'url', 'file', 'title', 'created_at', 'updated_at')
