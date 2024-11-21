from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=100)
    created_date = models.DateTimeField()
    last_login = models.DateTimeField()

    def __str__(self):
        return self.user_name
