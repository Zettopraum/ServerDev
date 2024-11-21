from django.urls import path
from content.api.views import ContentList, ContentRetrieve, ContentCreate, ContentUpdate, ContentDestroy

urlpatterns = [
    path('v1/content/', ContentList.as_view(), name='content-list'),
    path('v1/content/<id>/', ContentRetrieve.as_view(), name='content-detail'),
    path('v1/content/create/', ContentCreate.as_view(), name='content-create'),
    path('v1/content/<id>/update/', ContentUpdate.as_view(), name='content-update'),
    path('v1/content/<id>/delete/', ContentDestroy.as_view(), name='content-destroy'),
] 