from django.db.models import query
from url_parser import parse_url
from .models import Document, Image, Video, Audio
from rest_framework import  viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import DocumentSerializer, ImageSerializer, VideoSerializer, AudioSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    serializer_class = DocumentSerializer
    parser_classes = (MultiPartParser, FormParser,)

    queryset = Document.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = DocumentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response("documento criado!", status=status.HTTP_201_CREATED, headers=headers)
        

class VideoViewSet(viewsets.ModelViewSet):
    serializer_class = VideoSerializer
    queryset = Video.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = VideoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        link_video = parse_url(serializer.validated_data.get('link_video'))
        title = serializer.validated_data.get('title')
        link_video_id= link_video['query']['v']
        serializer.save(title=title, link_video=link_video_id)
        
        

class AudioViewSet(viewsets.ModelViewSet):
    serializer_class = AudioSerializer
    parser_classes = (MultiPartParser, FormParser,)
    queryset = Audio.objects.all()
    # permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = AudioSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response("Áudio criado com sucesso", status=status.HTTP_201_CREATED, headers=headers)


class ImageViewSet(viewsets.ModelViewSet):
    serializer_class = ImageSerializer
    parser_classes = (MultiPartParser, FormParser,)
    queryset = Image.objects.all()
