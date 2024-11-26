from rest_framework import serializers
from user.serializers import UserSerializer
from content.serializers import ContentSerializer
from watchlist.models import Watchlist

class WatchlistSerializer(serializers.ModelSerializer):
    user_id = UserSerializer()  
    content_id = ContentSerializer()  

    class Meta:
        model = Watchlist
        fields = ['user','content','added_date','user_id','content_id']