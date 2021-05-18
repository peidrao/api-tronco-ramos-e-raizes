from django.urls import path
from .views import DocumentView

urlpatterns = [
    path('upload/', DocumentView.as_view(), name='file-upload')
]
