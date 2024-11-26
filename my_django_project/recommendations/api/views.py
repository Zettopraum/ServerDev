from rest_framework import generics
from recommendations.models.recommendations import Recommendations
from recommendations.serializers.recommendations import RecommendationsSerializer
from drf_spectacular.utils import extend_schema
 
@extend_schema(summary="Отримання списку всіх рекомендацій.")
class RecommendationsList(generics.ListAPIView):
    queryset = Recommendations.objects.all()
    serializer_class = RecommendationsSerializer
    

@extend_schema(summary="Отримання конкретної рекомендації.")
class RecommendationsRetrieve(generics.RetrieveAPIView):
    queryset = Recommendations.objects.all()
    serializer_class = RecommendationsSerializer


@extend_schema(summary="Створення нової рекомендації.")
class RecommendationsCreate(generics.CreateAPIView):
    queryset = Recommendations.objects.all()
    serializer_class = RecommendationsSerializer


@extend_schema(summary="Оновлення даних рекомендації.")
class RecommendationsUpdate(generics.UpdateAPIView):
    queryset = Recommendations.objects.all()
    serializer_class = RecommendationsSerializer
    

@extend_schema(summary="Видалення конкретної рекомендації.")
class RecommendationsDestroy(generics.DestroyAPIView):
    queryset = Recommendations.objects.all()
    serializer_class = RecommendationsSerializer