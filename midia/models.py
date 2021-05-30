from django.db import models
from .validators import validate_file_size, UploadToPath
from .models_abs import AlbumAbs, ModelAbs



class Document(ModelAbs):
    file = models.FileField(upload_to=UploadToPath('documents'), validators=[validate_file_size], blank=False, null=False)
    
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
        return str(self.title)

class Audio(AlbumAbs):
    audios = models.ForeignKey(AlbumAudio, default=None, on_delete=models.CASCADE)
    audio_album = models.FileField(upload_to=UploadToPath('audios'), validators=[validate_file_size], blank=False, null=False)
    
    def __str__(self):
        return self.title

class Video(AlbumAbs):
    videos = models.ForeignKey(AlbumVideo, default=None, on_delete=models.CASCADE)
    video_album = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Image(AlbumAbs):
    images = models.ForeignKey(AlbumImage, default=None, on_delete=models.CASCADE)
    image_album = models.FileField(upload_to=UploadToPath('images'))
    
    def __str__(self):
        return self.title 