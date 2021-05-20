from rest_framework import  serializers
from .models import Document, Video, Audio


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('id', 'file', 'title', 'created_at', 'updated_at')


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('id', 'link_video', 'title', 'created_at', 'updated_at')


class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields = ('id', 'file', 'name', 'created_at', 'updated_at')
    