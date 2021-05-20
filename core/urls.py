
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework import routers

from document.views import DocumentViewSet
from video.views import VideoViewSet

router = routers.DefaultRouter()

router.register(r'api/v1/document', DocumentViewSet, basename='document')
router.register(r'api/v1/video', VideoViewSet, basename='video')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
    # path('', include('video.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)