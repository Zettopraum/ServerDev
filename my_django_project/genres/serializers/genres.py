from rest_framework import serializers
from genres.models import Genres

class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = ['id','name'] 
