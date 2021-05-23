from django.contrib import admin
from .models import Document, Image, Video, Audio


class DocumentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ['__str__', 'created_at', 'updated_at']

    class Meta:
        model = Document


class VideoAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'created_at', 'updated_at']

    class Meta:
        model = Video


class AudioAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ['__str__', 'created_at', 'updated_at']

    class Meta:
        model = Audio



class ImageAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ['__str__', 'created_at', 'updated_at']

    class Meta:
        model = Image


admin.site.register(Document, DocumentAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Audio, AudioAdmin)
#admin.site.register(Image, ImageAdmin)