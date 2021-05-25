from rest_framework import viewsets
from .models_abs import Tag
from .serializers import *
from .models import *


class TagViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()


class DocumentViewSet(viewsets.ModelViewSet):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()


class AlbumAudioViewSet(viewsets.ModelViewSet):
    serializer_class = AlbumAudioSerializer
    queryset = AlbumAudio.objects.all()



class AudioViewSet(viewsets.ModelViewSet):
    serializer_class = AudioSerializer
    queryset = Audio.objects.all()


class AlbumVideoViewSet(viewsets.ModelViewSet):
    serializer_class = AlbumVideoSerializer
    queryset = AlbumVideo.objects.all()


class VideoViewSet(viewsets.ModelViewSet):
    serializer_class = VideoSerializer
    queryset = Video.objects.all()


class AlbumImageViewSet(viewsets.ModelViewSet):
    serializer_class = AlbumImageSerializer
    queryset = AlbumImage.objects.all()


class ImageViewSet(viewsets.ModelViewSet):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()