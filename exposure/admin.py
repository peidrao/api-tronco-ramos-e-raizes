from exposure.models import Exposure
from django.contrib import admin

class ExposureAdmin(admin.ModelAdmin):
    list_display = ['title', 'user']
    search_fields = ('title__startswith',)

# Register your models here.
admin.site.register(Exposure, ExposureAdmin)


