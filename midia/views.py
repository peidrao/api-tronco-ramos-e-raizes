from .models import Document, Video, Audio
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import DocumentSerializer, VideoSerializer, AudioSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    serializer_class = DocumentSerializer
    parser_classes = (MultiPartParser, FormParser,)

    queryset = Document.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = DocumentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response("Documento criado com sucesso", status=status.HTTP_201_CREATED, headers=headers)


class VideoViewSet(viewsets.ModelViewSet):
    serializer_class = VideoSerializer
    queryset = Video.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = VideoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response("Vídeo criado com sucesso", status=status.HTTP_201_CREATED, headers=headers)


class AudioViewSet(viewsets.ModelViewSet):
    serializer_class = AudioSerializer
    parser_classes = (MultiPartParser, FormParser,)
    queryset = Audio.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = AudioSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response("Áudio criado com sucesso", status=status.HTTP_201_CREATED, headers=headers)