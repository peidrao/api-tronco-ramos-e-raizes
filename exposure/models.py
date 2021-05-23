from midia.models import Audio, Document, Image, Video
from user.models import User
from model_abs import ModelAbs
from django.db import models


class Tag(models.Model):
    title = models.CharField(max_length=50)
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class AlbumAbs(models.Model):
    class Meta:
        abstract = True


    title = models.CharField(max_length=250)
    tags = models.ForeignKey(Tag, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class AlbumImage(AlbumAbs):
    album = models.ForeignKey(Image, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'images/')
 
 

class Exposure(models.Model):
    title = models.CharField(max_length=200)
    legend = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    tags = models.ForeignKey(Tag, on_delete=models.CASCADE)
    album_image = models.OneToOneField(AlbumImage, on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    