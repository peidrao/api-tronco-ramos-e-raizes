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
    isPublic = models.CharField(
        max_length=20, choices=IS_PUBLIC, default="Arquivar", verbose_name='Status de publicação')
    users = models.ManyToManyField(User, verbose_name='Usuários')
    albumImage = models.OneToOneField(
        AlbumImage, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Álbum de imagem')
    albumVideo = models.OneToOneField(
        AlbumVideo, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Álbum de video')
    albumAudio = models.OneToOneField(
        AlbumAudio, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Álbum de áudio')
    
    views = models.PositiveIntegerField('Quantidade de visualizações!')
    lat = models.CharField('Latitude', max_length=50)
    long = models.CharField('Longitude', max_length=50)


    
    thumbnail = models.ImageField(upload_to=UploadToPath('thumbail_exposure'))
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Exposições'
        verbose_name_plural = 'Exposições'
