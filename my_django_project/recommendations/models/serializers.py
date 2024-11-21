from rest_framework import serializers
from user.models.serializers import UserSerializer
from content.models.serializers import ContentSerializer
from recommendations.models import Recommendations

class RecommendationsSerializer(serializers.ModelSerializer):
    user_id = UserSerializer()  
    content_id = ContentSerializer()  

    class Meta:
        model = Recommendations
        fields = '__all__'  
