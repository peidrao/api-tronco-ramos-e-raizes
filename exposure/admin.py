import admin_thumbnails
from django.contrib import admin

from .models import *

class AlbumImageAdmin(admin.StackedInline):
    model = AlbumImage
 
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    inlines = [AlbumImageAdmin]
 
    class Meta:
       model = Image
 
@admin.register(AlbumImage)
class AlbumImageAdmin(admin.ModelAdmin):
    pass

@admin.register(Exposure)
class Exposure(admin.ModelAdmin):
    pass