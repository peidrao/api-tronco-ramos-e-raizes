from exposure.models import Exposure
from django.contrib import admin

class ExposureAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ('title__startswith',)
    ordering = ("createdAt",)
    list_filter = ("isPublic", )

# Register your models here.
admin.site.register(Exposure, ExposureAdmin)


