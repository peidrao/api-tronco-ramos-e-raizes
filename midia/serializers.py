from rest_framework import  serializers
from .models import Document, Video, Audio, Image


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('id', 'user', 'file', 'title', 'created_at', 'updated_at')


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('id', 'user', 'link_video', 'title', 'created_at', 'updated_at')


class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields = ('id', 'user' ,'file', 'title', 'created_at', 'updated_at')
    

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'user' ,'image', 'title', 'created_at', 'updated_at')
