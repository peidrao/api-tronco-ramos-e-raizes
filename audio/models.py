from django.db import models
from model_abs import ModelAbs


class Audio(ModelAbs):
    file = models.FileField()
    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Áudio'
        verbose_name_plural = 'Áudios'
