from .models import Audio
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import AudioSerializer


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