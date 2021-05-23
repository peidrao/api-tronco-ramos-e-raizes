from django.contrib import admin
from .models import *
admin.site.register(Tag)

class DocumentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ['__str__', 'created_at', 'updated_at']



class VideoInline(admin.TabularInline):
    model = Video
    readonly_fields = ('id',)
    extra = 1

class AlbumVideoAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'created_at', 'updated_at']
    inlines = [VideoInline]
    

class AudioInline(admin.TabularInline):
    model = Audio
    readonly_fields = ('id',)
    extra = 1


class AlbumAudioAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ['__str__', 'created_at', 'updated_at']
    inlines= [AudioInline]

class ImageInline(admin.TabularInline):
    model = Image
    readonly_fields = ('id',)
    extra = 1

class AlbumImageAdmin(admin.ModelAdmin):
    fields = ("title",)
    inlines = [ImageInline]


admin.site.register(AlbumImage, AlbumImageAdmin)
admin.site.register(Image)

admin.site.register(Document, DocumentAdmin)

admin.site.register(AlbumAudio, AlbumAudioAdmin)
admin.site.register(Audio)

admin.site.register(AlbumVideo, AlbumVideoAdmin)
admin.site.register(Video)
 