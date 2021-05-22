from .serializers import TaskSerializer
from .models import Task
from rest_framework import request, viewsets
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class UploadViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


""" 
class PhotoViewSet(viewsets.ModelViewSet):
    serializer_class = FileListSerializer
    parser_classes = (MultiPartParser, FormParser,)
    queryset=Photo.objects.all()

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs) """


""" class BlogsViewSet(viewsets.ModelViewSet):
    serializer_class = BlogsSerializer
    queryset = Blogs.objects.all()

    def create(self, request, *args, **kwargs):
        instance_data = request.data
        data = {key: value for key, value in instance_data.items()}
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()

        if request.FILES:
            photos = dict((request.FILES).lists()).get('photos', None)
            if photos:
                for photo in photos:
                    photo_data = {}
                    photo_data["blogs"] = instance.pk
                    photo_data["image"] = photo
                    photo_serializer = PhotoSerializer(data=photo_data)
                    photo_serializer.is_valid(raise_exception=True)
                    photo_serializer.save()

        return Response(serializer.data) """


""" class PostView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        posts_serializer = PostSerializer(data=request.data)
        if posts_serializer.is_valid():
            posts_serializer.save()
            return Response(posts_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', posts_serializer.errors)
            return Response(posts_serializer.errors, status=status.HTTP_400_BAD_REQUEST) """