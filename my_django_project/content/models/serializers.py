from rest_framework import serializers
from genres.models.serializers import GenresSerializer  
from content.models import Content

class ContentSerializer(serializers.ModelSerializer):
    genre_id = GenresSerializer() 

    class Meta:
        model = Content
        fields = '__all__'  
