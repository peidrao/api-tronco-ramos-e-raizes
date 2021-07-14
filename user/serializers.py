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
            'image_profile',
            "email",
            "is_staff",
            "is_active",
            "is_superuser",
            'updatedAt',
            'password',
            # "user_permissions",
            'albumImage',
            'images'
        )
