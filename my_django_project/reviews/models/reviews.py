from django.db import models
from user.models import User
from content.models.content import Content


class Reviews(models.Model):
    user = models.ForeignKey("user.User", on_delete=models.CASCADE, related_name="reviews")
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name="reviews")
    rating = models.IntegerField()
    comment = models.TextField()
    review_date = models.DateTimeField()
    
    def __str__(self):
        return f"Review by {self.user.user_name} on {self.content.title}"

