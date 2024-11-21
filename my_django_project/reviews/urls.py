from django.urls import path
from reviews.api.views import ReviewsList, ReviewsRetrieve, ReviewsCreate, ReviewsUpdate, ReviewsDestroy

urlpatterns = [
    path('v1/reviews/', ReviewsList.as_view(), name='reviews-list'),
    path('v1/reviews/<id>/', ReviewsRetrieve.as_view(), name='reviews-detail'),
    path('v1/reviews/create/', ReviewsCreate.as_view(), name='reviews-create'),
    path('v1/reviews/<id>/update/', ReviewsUpdate.as_view(), name='reviews-update'),
    path('v1/reviews/<id>/delete/', ReviewsDestroy.as_view(), name='reviews-destroy'),
] 