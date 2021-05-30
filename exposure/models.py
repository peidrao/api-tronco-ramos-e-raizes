from user.models import User
from django.db import models
from django.db.models.base import Model
from midia.models import AlbumAudio, AlbumImage, AlbumVideo
from midia.models_abs import Tag

IS_PUBLIC = (
    ("ARQUIVAR", "Arquivar"),
    ("PUBLICAR", "Publicar"),
)


class Exposure(models.Model):
    title = models.CharField(max_length=200)
    legend = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    tags= models.ManyToManyField(Tag)
    is_public = models.CharField(max_length=20, choices=IS_PUBLIC, default="Arquivar")
    users = models.ManyToManyField(User)
    album_image = models.OneToOneField(AlbumImage, on_delete=models.CASCADE)
    album_video = models.OneToOneField(AlbumVideo, on_delete=models.CASCADE)
    album_audio = models.OneToOneField(AlbumAudio, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Exposições'
        verbose_name_plural = 'Exposições'


