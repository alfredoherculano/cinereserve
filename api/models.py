from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=50, unique=True, null=False)
    length = models.IntegerField(null=False)
    theme = models.CharField(max_length=15, null=False)

    def __str__(self):
        return self.title
    
class Session(models.Model):
    date = models.DateTimeField(null=False)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.date