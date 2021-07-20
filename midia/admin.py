from django import forms
from url_parser import parse_url
from django.contrib.auth.models import Group
from django.contrib import admin
from .models import *
from .models_abs import Tag

class TagAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'colorTag']

class DocumentAdmin(admin.ModelAdmin):
    date_hierarchy = 'createdAt'
    list_display = ['__str__', 'createdAt', 'updatedAt']

class VideoInline(admin.TabularInline):
    model = Video
    fields = ("title", "description", "tags",  "videoUrl", "author", "user",)
    readonly_fields = ('id',)
    extra = 1


class AlbumVideoAdmin(admin.ModelAdmin):
    model = AlbumVideo
    fields = ("title", "isPublic", "user", "lat", "long")
    inlines = [VideoInline]

class AudioInline(admin.TabularInline):
    model = Audio
    fields = ("title", "description", "tags",  "audio", "author", "user",)
    readonly_fields = ('id',)
    extra = 1


class AlbumAudioAdmin(admin.ModelAdmin):
    model = AlbumImage
    fields = ("title", "isPublic", "user", "lat", "long")
    date_hierarchy = 'createdAt'
    list_display = ['__str__', 'createdAt', 'updatedAt']
    inlines= [AudioInline]




class AlbumImageInline(admin.TabularInline):
    model = Image
    fields = ("title", "description", "tags",  "image", "author", "user",)
    readonly_fields = ('id',)
 

class AlbumImageAdmin(admin.ModelAdmin):

    fields = ("title", "isPublic", "user", "lat", "long")
    list_display = ['__str__', 'isPublic', 'user']
    inlines = [AlbumImageInline]


class ImageAdmin(admin.ModelAdmin):
    model = Image
    list_display = ['title', 'author', 'image_url']




admin.site.register(AlbumImage, AlbumImageAdmin)
admin.site.register(Image, ImageAdmin)

admin.site.register(Document, DocumentAdmin)
admin.site.register(Tag, TagAdmin)

admin.site.register(AlbumAudio, AlbumAudioAdmin)
admin.site.register(Audio)

admin.site.register(AlbumVideo, AlbumVideoAdmin)
admin.site.register(Video)

admin.site.unregister(Group)
