from user.models import User
from exposure.models import Exposure
from rest_framework import serializers
from midia.serializers import AlbumImageSerializer, AlbumVideoSerializer, AlbumAudioSerializer, TagSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "name", "username", "email"]

class ExposureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exposure
        fields = "__all__" 

    
    def to_representation(self, instance):
        self.fields['albumImage'] = AlbumImageSerializer(read_only=True, many=False)
        self.fields['albumAudio'] = AlbumAudioSerializer(read_only=True, many=False)
        self.fields['albumVideo'] = AlbumVideoSerializer(read_only=True, many=False)
        self.fields['users'] = UserSerializer(read_only=True, many=True)
        self.fields['tags'] = TagSerializer(read_only=True, many=True)
        return super().to_representation(instance)


class GeoSerializer(serializers.ModelSerializer):

    class Meta:
        model = 