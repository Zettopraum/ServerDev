from rest_framework import serializers
from genres.serializers import GenresSerializer  
from content.models import Content

class ContentSerializer(serializers.ModelSerializer):
    genre_id = GenresSerializer() 

    class Meta:
        model = Content
        fields = ['id','genre_id','title','description','release_date','rating']