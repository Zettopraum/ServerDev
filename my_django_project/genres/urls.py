from django.urls import path
from genres.api.views import GenresList, GenresRetrieve, GenresCreate, GenresUpdate, GenresDestroy

urlpatterns = [
    path('v1/genres/', GenresList.as_view(), name='genres-list'),
    path('v1/genres/<id>/', GenresRetrieve.as_view(), name='genres-detail'),
    path('v1/genres/create/', GenresCreate.as_view(), name='genres-create'),
    path('v1/genres/<id>/update/', GenresUpdate.as_view(), name='genres-update'),
    path('v1/genres/<id>/delete/', GenresDestroy.as_view(), name='genres-destroy'),
] 