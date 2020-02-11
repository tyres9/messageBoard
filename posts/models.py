from django.db import models
from datetime import date
from django.contrib.auth.models import User



# Create your models here.
class Post(models.Model):
    text = models.TextField()
    date_posted = models.DateField(default = date.today)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:50]
        