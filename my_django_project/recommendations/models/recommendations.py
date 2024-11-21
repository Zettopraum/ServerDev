from django.db import models
from user.models import User
from content.models import Content

class Recommendations(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recommendations")
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name="recommendations")
    recommended_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Recommendation for {self.user.user_name}: {self.content.title}"