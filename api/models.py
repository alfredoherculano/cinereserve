from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=50, unique=True, null=False)
    length = models.IntegerField(null=False)
    theme = models.CharField(max_length=15, null=False)
