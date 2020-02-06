from django.db import models

# Create your models here.


class File(models.Model):

    filename = models.CharField(max_length=100)
    category = models.CharField(max_length=20)
    genre = models.CharField(max_length=20)
    file = models.FileField()
    author = models.CharField(default="", max_length=50)