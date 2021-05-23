from rest_framework import serializers
from .models import *
from .models_abs import Tag


class TagSerializer(serializers.Serializer):
    class Meta: 
        model = Tag
        fields = ("title", "color")