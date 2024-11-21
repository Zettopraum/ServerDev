from django.db import models
from user.models import User
from content.models import Content

class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="watchlist")
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name="watchlists")
    added_date = models.DateTimeField()
    
    def __str__(self):
        return f"{self.user.user_name}'s watchlist item: {self.content.title}"