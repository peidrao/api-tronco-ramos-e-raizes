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

""" class VideoForm(forms.ModelForm):
    class Meta: 
        model = AlbumVideo
        fields = "__all__"
        
def clean_video_album(self):
        link_video = parse_url(self.clean_data['video_album'])
        print(link_video)
        print('asdasdasd')
        return self.cleaned_data['video_album']


def perform_create(self, serializer):
    link_video = parse_url(serializer.validated_data.get('link_video'))
    title = serializer.validated_data.get('title')
    link_video_id= link_video['query']['v']
    serializer.save(title=title, link_video=link_video_id) 
 """

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
    list_display = ['__str__']
    inlines = [AlbumImageInline]


admin.site.register(AlbumImage, AlbumImageAdmin)
admin.site.register(Image)

admin.site.register(Document, DocumentAdmin)
admin.site.register(Tag, TagAdmin)

admin.site.register(AlbumAudio, AlbumAudioAdmin)
admin.site.register(Audio)

admin.site.register(AlbumVideo, AlbumVideoAdmin)
admin.site.register(Video)

admin.site.unregister(Group)
