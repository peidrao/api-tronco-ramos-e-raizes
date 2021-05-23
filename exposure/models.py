from django.db import models
from midia.models import AlbumAudio, AlbumImage, AlbumVideo
from midia.models_abs import Tag

class Exposure(models.Model):
    title = models.CharField(max_length=200)
    legend = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    tags = models.ForeignKey(Tag, on_delete=models.CASCADE)
    album_image = models.OneToOneField(AlbumImage, on_delete=models.CASCADE)
    album_video = models.OneToOneField(AlbumVideo, on_delete=models.CASCADE)
    album_audio = models.OneToOneField(AlbumAudio, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


