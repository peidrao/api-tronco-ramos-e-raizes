from exposure.models import Exposure
from django.contrib import admin

class ExposureAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ('title__startswith',)
    ordering = ("created_at",)
    list_filter = ("is_public", )

# Register your models here.
admin.site.register(Exposure, ExposureAdmin)


