from django.db import models


# Create your models here.

class Video(models.Model):
    title = models.CharField(max_length=100)
    link_video = models.CharField(max_length=250)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)