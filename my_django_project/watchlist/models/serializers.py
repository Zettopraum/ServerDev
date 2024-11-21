from rest_framework import serializers
from user.models.serializers import UserSerializer
from content.models.serializers import ContentSerializer
from watchlist.models import Watchlist

class WatchlistSerializer(serializers.ModelSerializer):
    user_id = UserSerializer()  
    content_id = ContentSerializer()  

    class Meta:
        model = Watchlist
        fields = '__all__'  
