from rest_framework import serializers
from .models import Movie, Profile, Session, Seat
from django.contrib.auth import get_user_model

Profile = get_user_model()

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        instance = Profile.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        
        return instance

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'length', 'theme']

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ['id', 'date', 'movie']

class SeatSerializer(serializers.ModelSerializer):
    movie = serializers.CharField(source='session.movie.title', read_only=True)

    class Meta:
        model = Seat
        fields = ['id', 'session', 'movie', 'seat_number', 'status']