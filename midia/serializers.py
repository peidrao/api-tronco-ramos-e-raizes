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

    def to_representation(self, instance):
        self.fields['tags'] = TagSerializer(read_only=True, many=True)
        return super().to_representation(instance)



class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields = "__all__"

    def to_representation(self, instance):
        self.fields['tags'] = TagSerializer(read_only=True, many=True)
        return super().to_representation(instance)


class AlbumAudioSerializer(serializers.ModelSerializer):
    audios = AudioSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = AlbumAudio
        fields = ("id", "title", "user", "audios", 'tags')


class VideoSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Video
        fields = ("id", "album", 'user', 'videoUrl', 'tags')

    def to_representation(self, instance):
        self.fields['tags'] = TagSerializer(read_only=True, many=True)
        return super().to_representation(instance)


class AlbumVideoSerializer(serializers.ModelSerializer):
    videos = VideoSerializer(many=True, read_only=True)

    class Meta:
        model = AlbumVideo
        fields = ("id", 'title', 'user', 'videos')


class ImageSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Image
        fields = ("id", "album", "user", "title", "author", "image", 'tags')

    def to_representation(self, instance):
        self.fields['tags'] = TagSerializer(read_only=True, many=True)
        return super().to_representation(instance)


class AlbumImageSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = AlbumImage
        fields = ("id", 'title', 'user', 'images')
