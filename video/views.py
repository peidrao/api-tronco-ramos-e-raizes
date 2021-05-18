from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import VideoSerializer



class VideoView(APIView):
    parser_classes = (MultiPartParser, FormParser)


    def post(self, request):
        video_serializer = VideoSerializer(data=request.data)
        if video_serializer.is_valid():
            video_serializer.save()
            return Response(video_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(video_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
