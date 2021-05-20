""" from django.urls import path
from .views import VideoView

urlpatterns = [
    path('create/', VideoView.as_view(), name='video-create')
] """