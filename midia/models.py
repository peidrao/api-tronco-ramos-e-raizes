from django.db import models

from .validators import validate_file_size

class Tag(models.Model):
    title = models.CharField(max_length=50)
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Document(models.Model):
    file = models.FileField(upload_to='documents', validators=[validate_file_size], blank=False, null=False)
    title = models.CharField(max_length=250)
   # user = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)
    
    class Meta:
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'


class AlbumAudio(models.Model):
    title = models.CharField(max_length=250)
      
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)

class Audio(models.Model):
    audios = models.ForeignKey(AlbumAudio, default=None, on_delete=models.CASCADE)
    file = models.FileField(upload_to='audios', validators=[validate_file_size], blank=False, null=False)
    title = models.CharField(max_length=250)
    tags = models.ForeignKey(Tag, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class AlbumVideo(models.Model):
    title = models.CharField(max_length=250)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)


class Video(models.Model):
    video = models.ForeignKey(AlbumVideo, default=None, on_delete=models.CASCADE)
    link_video = models.CharField(max_length=200)

    title = models.CharField(max_length=250)
    tags = models.ForeignKey(Tag, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class AlbumImage(models.Model):
    title = models.CharField(max_length=250)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)

class Image(models.Model):
    image = models.ForeignKey(AlbumImage, default=None, on_delete=models.CASCADE)
    image_album = models.FileField(upload_to = 'album_images/')

    title = models.CharField(max_length=250)
    tags = models.ForeignKey(Tag, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title 