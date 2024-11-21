from django.urls import path
from watchlist.api.views import WatchlistList, WatchlistRetrieve, WatchlistCreate, WatchlistUpdate, WatchlistDestroy

urlpatterns = [
    path('v1/watchlist/', WatchlistList.as_view(), name='watchlist-list'),
    path('v1/watchlist/<id>/', WatchlistRetrieve.as_view(), name='watchlist-detail'),
    path('v1/watchlist/create/', WatchlistCreate.as_view(), name='watchlist-create'),
    path('v1/watchlist/<id>/update/', WatchlistUpdate.as_view(), name='watchlist-update'),
    path('v1/watchlist/<id>/delete/', WatchlistDestroy.as_view(), name='watchlist-destroy'),
] 