from rest_framework import serializers
from .models import MovieOrder
from movies.models import Movie
from users.models import User


class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    purchased_at = serializers.DateTimeField(read_only=True)
    title = serializers.SerializerMethodField()
    purchased_by = serializers.SerializerMethodField()

    def get_title(self, obj: Movie):
        return obj.movie.title

    def get_purchased_by(self, obj: User):
        return obj.user.email

    def create(self, validated_data):
        return MovieOrder.objects.create(**validated_data)
