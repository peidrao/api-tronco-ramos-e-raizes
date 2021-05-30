from rest_framework import serializers
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
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
            "password"
            )