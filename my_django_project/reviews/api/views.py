from rest_framework import generics
from reviews.models.reviews import Reviews
from reviews.serializers.serializers import ReviewsSerializer
from drf_spectacular.utils import extend_schema

@extend_schema(summary="Отримання списку всіх рецензій.")
class ReviewsList(generics.ListAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
    

@extend_schema(summary="Отримання конкретної рецензії.")
class ReviewsRetrieve(generics.RetrieveAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer


@extend_schema(summary="Створення нової рецензії.")
class ReviewsCreate(generics.CreateAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer


@extend_schema(summary="Оновлення інформації про рецензію.")
class ReviewsUpdate(generics.UpdateAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
    

@extend_schema(summary="Видалення конкретної рецензії.")
class ReviewsDestroy(generics.DestroyAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer