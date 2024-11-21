from rest_framework import serializers
from user.models.serializers import UserSerializer
from content.models.serializers import ContentSerializer
from reviews.models import Reviews

class ReviewsSerializer(serializers.ModelSerializer):
    user_id = UserSerializer()  
    content_id = ContentSerializer()  

    class Meta:
        model = Reviews
        fields = '__all__'  
