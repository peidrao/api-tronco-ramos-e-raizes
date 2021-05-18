from django.contrib import admin
from .models import Video

# Register your models here.

class VideoAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'created_at', 'updated_at']

    class Meta:
        model = Video


admin.site.register(Video, VideoAdmin)