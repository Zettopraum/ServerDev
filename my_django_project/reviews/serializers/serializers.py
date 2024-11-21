from rest_framework import serializers
from user.serializers import UserSerializer
from content.serializers import ContentSerializer
from reviews.models import Reviews

class ReviewsSerializer(serializers.ModelSerializer):
    user_id = UserSerializer()  
    content_id = ContentSerializer()  

    class Meta:
        model = Reviews
        fields = ['user','content','rating','comment','review_date']