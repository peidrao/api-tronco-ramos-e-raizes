from rest_framework import serializers
from .models import *
from .models_abs import Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Tag
        fields = "__all__"