from rest_framework import serializers
from .models import *
from .models_abs import Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Tag
        fields = "__all__"


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = "__all__"

class AlbumAudioSerializer(serializers.ModelSerializer):
    class Meta: 
        model = AlbumAudio
        fields = "__all__"

class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields = "__all__"


class AlbumVideoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = AlbumVideo
        fields = "__all__"

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = "__all__"


class AlbumImageSerializer(serializers.ModelSerializer):
    class Meta: 
        model = AlbumImage
        fields = "__all__"

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"



