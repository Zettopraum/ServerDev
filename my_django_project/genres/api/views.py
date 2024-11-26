from rest_framework import generics
from genres.models.genres import Genres
from genres.serializers.genres import GenresSerializer
from drf_spectacular.utils import extend_schema
 
@extend_schema(summary="Отримання списку всіх жанрів.")
class GenresList(generics.ListAPIView):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer
    

@extend_schema(summary="Отримання конкретного жанру.")
class GenresRetrieve(generics.RetrieveAPIView):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer


@extend_schema(summary="Створення нового жанру.")
class GenresCreate(generics.CreateAPIView):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer


@extend_schema(summary="Оновлення інформації про жанр.")
class GenresUpdate(generics.UpdateAPIView):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer
    

@extend_schema(summary="Видалення конкретного жанру.")
class GenresDestroy(generics.DestroyAPIView):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer