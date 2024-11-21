from django.urls import path
from recommendations.api.views import RecommendationsList, RecommendationsRetrieve, RecommendationsCreate, RecommendationsUpdate, RecommendationsDestroy

urlpatterns = [
    path('v1/recommendations/', RecommendationsList.as_view(), name='recommendations-list'),
    path('v1/recommendations/<id>/', RecommendationsRetrieve.as_view(), name='recommendations-detail'),
    path('v1/recommendations/create/', RecommendationsCreate.as_view(), name='recommendations-create'),
    path('v1/recommendations/<id>/update/', RecommendationsUpdate.as_view(), name='recommendations-update'),
    path('v1/recommendations/<id>/delete/', RecommendationsDestroy.as_view(), name='recommendations-destroy'),
] 