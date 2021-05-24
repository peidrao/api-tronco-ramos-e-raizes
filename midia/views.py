from rest_framework import viewsets
from .serializers import TagSerializer
from .models_abs import Tag

class TagViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    print(queryset)



