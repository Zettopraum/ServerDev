from django.db import models
from genres.models.genres import Genres

class Content(models.Model):
    genre_id=models.ForeignKey(Genres, verbose_name=("contents"), on_delete=models.CASCADE)
    title=models.CharField(max_length=150)
    description=models.TextField()
    release_date=models.DateField()
    rating=models.IntegerField()
    
    def __str__(self):
        return self.title
    