from midia.models import AlbumAudio
from exposure.models import Exposure
from rest_framework import serializers
from midia.serializers import AlbumImageSerializer, AlbumVideoSerializer, AlbumAudioSerializer


class ExposureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exposure
        fields = "__all__" 

    
    def to_representation(self, instance):
        self.fields['album_image'] = AlbumImageSerializer(read_only=True, many=False)
        self.fields['album_audio'] = AlbumAudioSerializer(read_only=True, many=False)
        self.fields['album_video'] = AlbumVideoSerializer(read_only=True, many=False)
        return super().to_representation(instance)
