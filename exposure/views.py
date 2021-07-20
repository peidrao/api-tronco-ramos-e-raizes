from django.shortcuts import render
from rest_framework.views import APIView

from django.http import JsonResponse
# Create your views here.
from exposure.models import *
from exposure.serializers import *
from midia.serializers import *
from midia.models import *

from rest_framework import viewsets
from rest_framework.response import Response
from drf_multiple_model.views import ObjectMultipleModelAPIView


class ExposureViewSet(viewsets.ModelViewSet):
    serializer_class = ExposureSerializer
    queryset = Exposure.objects.all()



class PointsGeoView(APIView):
    def get(self, request, format=None):
        exposure_serializer = ExposureGeoLocationSerializer(Exposure.objects.all(), many=True)
        album_video_serializer = AlbumVideoGeoSerializer(AlbumVideo.objects.all(), many=True)
        album_audio_serializer = AlbumAudioGeoSerializer(AlbumAudio.objects.all(), many=True)
        album_image_serializer = AlbumImageGeoSerializer(AlbumImage.objects.all(), many=True)
        return JsonResponse({
            'exposure': exposure_serializer.data,
            'album_video': album_video_serializer.data,
            'album_audio': album_audio_serializer.data,
            'album_image': album_image_serializer.data,

            })


