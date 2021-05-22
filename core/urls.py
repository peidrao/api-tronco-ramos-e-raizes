
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from midia.views import DocumentViewSet, VideoViewSet, AudioViewSet
from user.views import UserViewSet, TokenIsValidViewSet
from exposure.views import UploadViewSet


router = routers.DefaultRouter()

router.register(r'api/v1/documents', DocumentViewSet, basename='document')
router.register(r'api/v1/videos', VideoViewSet, basename='video')
router.register(r'api/v1/audios', AudioViewSet, basename='audio')
router.register(r'api/v1/users', UserViewSet, basename='users')
router.register(r'api/v1/exposures', UploadViewSet, basename='exposure')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh' ),
    path('api/token_is_valid/', TokenIsValidViewSet.as_view(), name='token_is_valid' ),
   # path('api/v1/post/', PostView.as_view(), name='post' ),
    path('', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)