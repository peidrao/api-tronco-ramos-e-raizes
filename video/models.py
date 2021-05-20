from enum import unique
from django.db import models


# Create your models here.

class Video(models.Model):
    title = models.CharField(max_length=100, unique=True)
    link_video = models.CharField(max_length=250, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Vídeo'
        verbose_name_plural = 'Vídeos'