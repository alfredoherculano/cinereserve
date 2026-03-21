from django.db import models
from django.contrib.auth.models import AbstractUser

class Profile(AbstractUser):
    pass

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
        return str(self.date)
    
class Seat(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('reserved', 'Reserved'),
        ('purchased', 'Purchased'),
    ]

    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    seat_number = models.IntegerField(null=False)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='available')

    def __str__(self):
        return str(self.seat_number)