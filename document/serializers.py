from rest_framework import fields, serializers
from .models import Document

class DocumentSerializer(serializers.ModelSerializer):
    class Meta():
        model = Document
        fields = ('file', 'title', 'created_at', 'updated_at')
