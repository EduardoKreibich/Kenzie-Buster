from rest_framework import serializers
from .models import RatingMovie, Movie


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, required=False)
    rating = serializers.ChoiceField(
        choices=RatingMovie.choices,
        default=RatingMovie.G,
    )
    synopsis = serializers.CharField(required=False)
    added_by = serializers.SerializerMethodField()

    def get_added_by(self, obj: Movie):
        return obj.user.email

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
