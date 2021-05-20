from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import VideoSerializer
from .models import Video



class VideoViewSet(viewsets.ModelViewSet):
    serializer_class = VideoSerializer
    queryset = Video.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = VideoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response("Vídeo criado com sucesso", status=status.HTTP_201_CREATED, headers=headers)

"""     def post(self, request):
        video_serializer = VideoSerializer(data=request.data)
        print(request.data['link_video'])
        if video_serializer.is_valid():
            video_serializer.save()
            return Response(video_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(video_serializer.errors, status=status.HTTP_400_BAD_REQUEST) """
