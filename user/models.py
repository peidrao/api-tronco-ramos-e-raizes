from midia.validators import UploadToPath
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.hashers import make_password

# from model_abs import ModelAbs


class User(AbstractUser):
    name = models.CharField(verbose_name="Nome", max_length=150)
    image_profile = models.ImageField(
        verbose_name="Iamgem de perfil", upload_to=UploadToPath('image_profile_user'))

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.password.startswith('pbkdf2_sha256'):
            self.password = make_password(self.password)

        return super(User, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
