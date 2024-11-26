from rest_framework import generics
from watchlist.models.watchlist import Watchlist
from watchlist.serializers.watchlist import WatchlistSerializer
from drf_spectacular.utils import extend_schema

@extend_schema(summary="Отримання списку всіх списків перегляду.")
class WatchlistList(generics.ListAPIView):
    queryset = Watchlist.objects.all()
    serializer_class = WatchlistSerializer
    

@extend_schema(summary="Отримання конкретного списку перегляду.")
class WatchlistRetrieve(generics.RetrieveAPIView):
    queryset = Watchlist.objects.all()
    serializer_class = WatchlistSerializer


@extend_schema(summary="Створення нового списку перегляду.")
class WatchlistCreate(generics.CreateAPIView):
    queryset = Watchlist.objects.all()
    serializer_class = WatchlistSerializer


@extend_schema(summary="Оновлення даних списку перегляду.")
class WatchlistUpdate(generics.UpdateAPIView):
    queryset = Watchlist.objects.all()
    serializer_class = WatchlistSerializer
    

@extend_schema(summary="Видалення конкретного списку перегляду.")
class WatchlistDestroy(generics.DestroyAPIView):
    queryset = Watchlist.objects.all()
    serializer_class = WatchlistSerializer