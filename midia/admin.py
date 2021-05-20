from django.contrib import admin
from .models import Document, Video, Audio


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



admin.site.register(Document, DocumentAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Audio, AudioAdmin)