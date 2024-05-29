from django.db import models
from django.contrib.auth.models import User

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=100)  # e.g., 'Movie' or 'TV Show'
    

    def __str__(self):
        return f"{self.title} ({self.type}) - {self.user.username}"
