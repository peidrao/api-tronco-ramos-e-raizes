from django.db import models
from django.utils.safestring import mark_safe
from .validators import validate_file_size, UploadToPath
from .models_abs import AlbumAbs, ModelAbs, Tag
from user.models import User
from url_parser import parse_url


class Document(ModelAbs):
    file = models.FileField("Documento", upload_to=UploadToPath('documents'), validators=[
                            validate_file_size], blank=False, null=False)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'


class AlbumAudio(ModelAbs):
    def __str__(self):
        return self.title


class AlbumVideo(ModelAbs):

    def __str__(self):
        return str(self.title)

class AlbumImage(ModelAbs):

    def __str__(self):
        return self.title


class Audio(AlbumAbs):
    album = models.ForeignKey(
        AlbumAudio, related_name='audios', on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, related_name='audios', on_delete=models.CASCADE)
    audio = models.FileField('Fazer upload de áudio', upload_to=UploadToPath(
        'audios'),  validators=[validate_file_size])

    def __str__(self):
        return self.title


class Video(AlbumAbs):
    album = models.ForeignKey(
        AlbumVideo, related_name='videos', default=None, on_delete=models.CASCADE)
    video_url = models.CharField(max_length=200)
    user = models.ForeignKey(
        User, related_name='videos', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        link_video = parse_url(self.video_url)
        self.video_url = link_video['query']['v']
        return super(Video, self).save(*args, **kwargs)


class Image(AlbumAbs):
    album = models.ForeignKey(
        AlbumImage, related_name='images', on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=UploadToPath('images'))

    def __str__(self):
        return self.title


    def image_url(self):
        if not self.image:
            return ""
        else:
            return mark_safe('<img src="{}" width="50px" height="50px" />'.format(self.image.url))