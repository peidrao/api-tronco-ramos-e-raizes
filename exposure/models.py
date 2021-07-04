from midia.validators import UploadToPath
from user.models import User
from django.db import models
from midia.models import AlbumAudio, AlbumImage, AlbumVideo
from midia.models_abs import Tag


class Exposure(models.Model):
    IS_PUBLIC = (
        ("ARQUIVAR", "Arquivar"),
        ("PUBLICAR", "Publicar"),
    )

    title = models.CharField(
        verbose_name='Título da exposição', max_length=200)
    legend = models.CharField(
        verbose_name='Legenda da exposição', max_length=200)
    content = models.CharField(
        verbose_name='Descrição exposição', max_length=200)
    tags = models.ManyToManyField(Tag)
    is_public = models.CharField(
        max_length=20, choices=IS_PUBLIC, default="Arquivar", verbose_name='Status de publicação')
    users = models.ManyToManyField(User, verbose_name='Usuários')
    album_image = models.OneToOneField(
        AlbumImage, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Álbum de imagem')
    album_video = models.OneToOneField(
        AlbumVideo, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Álbum de video')
    album_audio = models.OneToOneField(
        AlbumAudio, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Álbum de áudio')
    
    thumbnail = models.ImageField(upload_to=UploadToPath('thumbail_exposure'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Exposições'
        verbose_name_plural = 'Exposições'
