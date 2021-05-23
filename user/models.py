from django.contrib.auth.models import AbstractUser
from django.db import models

# from model_abs import ModelAbs

class User(AbstractUser):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        