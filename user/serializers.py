from midia.serializers import AlbumImageSerializer, ImageSerializer
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    album_image = AlbumImageSerializer(many=True, read_only=True)
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = (
            "id", 
            "username",
            "name", 
            "email",
            "is_staff",
            "is_active",
            "is_superuser",
            #"created_at", 
            #"updated_at",
            #"user_permissions",
            'album_image',
            'images',
            'password'
            )
    