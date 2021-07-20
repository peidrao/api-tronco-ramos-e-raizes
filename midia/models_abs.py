
from django.db import models
from django.utils import safestring
#from django.utils.safestring import mark_safe
from django.utils.html import format_html
from user.models import User


class Tag(models.Model):
    title = models.CharField("Título da tag", max_length=50)
    color = models.CharField("Cor da tag", max_length=50)

    def __str__(self):
        return self.title

    def colorTag(self):
        if self.color:
            return format_html('<p style="color: {}"`> Tag </p>', self.color)


class ModelAbs(models.Model):
    IS_PUBLIC = (
        ("ARQUIVAR", "Arquivar"),
        ("PUBLICAR", "Publicar"),
    )

    class Meta:
        abstract = True

    title = models.CharField('Título', max_length=100)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Usuário')
    isPublic = models.CharField('Status de publicação', max_length=20, choices=IS_PUBLIC,
                                 default="Arquivar")
    
    lat = models.CharField('Latitude', max_length=50)
    long = models.CharField('Longitude', max_length=50)
    views = models.PositiveBigIntegerField(default=0)

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)


class AlbumAbs(models.Model):
    class Meta:
        abstract = True

    title = models.CharField('Título do álbum', max_length=250)
    description = models.CharField('Descrição', max_length=250)
    tags = models.ManyToManyField(
        Tag, verbose_name='Tags do álbum')
    author = models.CharField('Autor do álbum', max_length=100)

   

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
