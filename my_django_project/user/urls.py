from django.urls import path
from user.api.views import UserList, UserRetrieve, UserCreate, UserUpdate, UserDestroy

urlpatterns = [
    path('v1/user/', UserList.as_view(), name='user-list'),
    path('v1/user/<id>/', UserRetrieve.as_view(), name='user-detail'),
    path('v1/user/create/', UserCreate.as_view(), name='user-create'),
    path('v1/user/<id>/update/', UserUpdate.as_view(), name='user-update'),
    path('v1/user/<id>/delete/', UserDestroy.as_view(), name='user-destroy'),
] 