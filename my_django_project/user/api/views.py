from rest_framework import generics
from user.models.user import User
from user.serializers.user import UserSerializer
from drf_spectacular.utils import extend_schema

@extend_schema(summary="Отримання списку всіх користувачів.")
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

@extend_schema(summary="Отримання конкретного користувача.")
class UserRetrieve(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@extend_schema(summary="Створення нового користувача.")
class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@extend_schema(summary="Оновлення інформації про користувача.")
class UserUpdate(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

@extend_schema(summary="Видалення користувача.")
class UserDestroy(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer