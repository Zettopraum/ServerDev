from rest_framework import serializers
from user.serializers import UserSerializer
from content.serializers import ContentSerializer
from recommendations.models import Recommendations

class RecommendationsSerializer(serializers.ModelSerializer):
    user_id = UserSerializer()  
    content_id = ContentSerializer()  

    class Meta:
        model = Recommendations
        fields = ['id','user','content','recommended_date','content_id','user_id']