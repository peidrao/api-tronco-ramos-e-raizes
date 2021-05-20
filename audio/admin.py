from django.contrib import admin

from .models import Audio

# Register your models here.

class AudioAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'

    list_display = ['__str__', 'created_at', 'updated_at']


    class Meta:
        model = Audio


admin.site.register(Audio, AudioAdmin)