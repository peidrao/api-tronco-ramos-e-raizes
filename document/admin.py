from django.contrib import admin

from .models import Document

# Register your models here.

class DocumentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'

    list_display = ['__str__', 'created_at', 'updated_at']


    class Meta:
        model = Document


admin.site.register(Document, DocumentAdmin)