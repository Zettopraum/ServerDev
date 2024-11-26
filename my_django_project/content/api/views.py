from rest_framework import generics
from content.models.content import Content
from content.serializers.content import ContentSerializer
from drf_spectacular.utils import extend_schema
 
@extend_schema(summary="Отримання списку всього контенту.")
class ContentList(generics.ListAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    

@extend_schema(summary="Отримання деталей конкретного контенту.")
class ContentRetrieve(generics.RetrieveAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer


@extend_schema(summary="Створення нового контенту.")
class ContentCreate(generics.CreateAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer


@extend_schema(summary="Оновлення даних контенту")
class ContentUpdate(generics.UpdateAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    

@extend_schema(summary="Видалення конкретного контенту.")
class ContentDestroy(generics.DestroyAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer