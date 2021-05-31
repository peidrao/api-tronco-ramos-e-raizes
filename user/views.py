# from user.models import User
from django.conf import settings
import jwt
from django.contrib.auth import get_user_model
from rest_framework import viewsets, views, exceptions
from rest_framework import status 
from rest_framework.response import Response
from  .models import User
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)        
        return Response('Usuário criado com sucesso!', status=status.HTTP_201_CREATED)

    def perform_create(self, request):
        user = get_user_model().objects.create(
            username=request.data['username'],
            name=request.data['name'],
            email=request.data['email'],
            is_staff=request.data['is_staff'],
            is_superuser=request.data['is_superuser']
        )
        user.set_password(request.data['password'])
        user.save()

class TokenIsValidViewSet(views.APIView):
    def get(self, request):
        return Response(request.data)


    def post(self, request, *args, **kwargs):
        try:
            token = request.data["access"]
            decode = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            print(decode)
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('access_token expired')
        except jwt.InvalidSignatureError:
            raise exceptions.AuthenticationFailed('access_token invalid token')
        except KeyError:
            raise exceptions.AuthenticationFailed('access_token invalid key')

        user = UserSerializer(User.objects.filter(id=decode["user_id"]).values()[0])
        decode.update(user.data)
        print(decode)
        return Response(decode)

