
from django.db import models
from django.utils import safestring
#from django.utils.safestring import mark_safe
from django.utils.html import format_html
from user.models import User


class Tag(models.Model):
    title = models.CharField(max_length=50)
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    def color_tag(self):
        if self.color:
            return format_html('<p style="color: {}"`> Tag </p>', self.color)
        


class ModelAbs(models.Model):
    
    class Meta:
        abstract = True

    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class AlbumAbs(models.Model):
    class Meta: 
        abstract = True

    title = models.CharField(max_length=250)
    tags = models.ForeignKey(Tag, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
