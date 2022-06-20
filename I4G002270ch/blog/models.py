from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class post(models.Model):
    Name = models.CharField(max_length=200)
    Text = models.TextField(max_length=300)
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    Created_date = models.DateTimeField()
    Published_date = models.DateTimeField()

    def __str__(self):
        return self.name
