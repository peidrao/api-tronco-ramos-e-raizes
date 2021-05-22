from os import write
from django.db.models import fields
from rest_framework import serializers

from .models import Task, TaskImage

class TaskImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskImage
        fields = ('image', 'id')



class TaskSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    images = TaskImageSerializer(source='taskimage_set', many=True, read_only=True)

    class Meta:
        model = Task
        fields = ('id', 'title', 'user', 'images')

    def create(self, validated_data):
        images_data = self.context.get('view').request.FILES
        task = Task.objects.create(title=validated_data.get('title', 'no-title'),
                                   user_id=1)
        for image_data in images_data.values():
            TaskImage.objects.create(task=task, image=image_data)
        return task



""" class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        fields = ['blogs', 'image',]


class BlogsSerializer(serializers.ModelSerializer):
    photos = serializers.SerializerMethodField()

    def get_photos(self, obj):
        photos = Photo.objects.filter(blogs=obj)
        return PhotoSerializer(photos, many=True, read_only=False).data

    class Meta:
        model = Blogs
        fields = "__all__" """


""" class PostSerializer(serializers.ModelSerializer):
    media = serializers.ListField(write_only=True, child=serializers.FileField(max_length=10000000,
                                                              allow_empty_file=True,
                                                              use_url=False))
    
    class Meta: 
        model = Post
        fields = '__all__'

    def is_valid(self, raise_exception=False):
        if len(self.data.getlist('image')) > 0:
            raise 'some error' """














#from .models import TaskImage, Task



""" class TaskImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskImage
        fields = ('image',)

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    images = TaskImageSerializer(source='taskimage_set', many=True, read_only=True)

    class Meta:
        model = Task
        fields = ('id', 'title', 'user', 'images')

    def create(self, validated_data):
        images_data = self.context.get('view').request.FILES
        task = Task.objects.create(title=validated_data.get('title', 'no-title'),
                                   user_id=1)
        for image_data in images_data.values():
            TaskImage.objects.create(task=task, image=image_data)
        return task """