from django import forms
from url_parser import parse_url
from django.contrib.auth.models import Group
from django.contrib import admin
from .models import *
from .models_abs import Tag

class TagAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'color_tag']

class DocumentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ['__str__', 'created_at', 'updated_at']

class VideoInline(admin.TabularInline):
    model = Video
    readonly_fields = ('id',)
    extra = 1


class AlbumVideoAdmin(admin.ModelAdmin):
    model = AlbumVideo
    
    inlines = [VideoInline]

class AudioInline(admin.TabularInline):
    model = Audio
    readonly_fields = ('id',)
    extra = 1


class AlbumAudioAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ['__str__', 'created_at', 'updated_at']
    inlines= [AudioInline]




class AlbumImageInline(admin.TabularInline):
    model = Image
    readonly_fields = ('id',)
 

class AlbumImageAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'is_public', 'user']
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
