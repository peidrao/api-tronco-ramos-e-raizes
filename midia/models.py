from django.db import models
from .validators import validate_file_size, UploadToPath
from .models_abs import AlbumAbs, ModelAbs
from user.models import User

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


class AlbumImage(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, related_name='albums', on_delete=models.CASCADE)

    def __str__(self):
        return self.title  

class Audio(AlbumAbs):
    album = models.ForeignKey(AlbumAudio, related_name='audios', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='audios', on_delete=models.CASCADE)
    audio = models.FileField(upload_to=UploadToPath('audios'),  validators=[validate_file_size],)
    
    def __str__(self):
        return self.title

class Video(AlbumAbs):
    album = models.ForeignKey(AlbumVideo, related_name='videos', default=None, on_delete=models.CASCADE)
    video_url = models.CharField(max_length=200)
    user = models.ForeignKey(User, related_name='videos', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Image(AlbumAbs):
    album = models.ForeignKey(AlbumImage, related_name='images', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=UploadToPath('images'))
    
    def __str__(self):
        return self.title 


