from rest_framework import serializers
from .models import Songs, Playlist, Rating


class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = ("title", "genre", "album", "artist")


class PlaylistSerializer(serializers.ModelSerializer):
    songs = serializers.PrimaryKeyRelatedField(many=True, read_only=False, queryset=Songs.objects.all())

    class Meta:
        model = Playlist
        fields = ("name", "songs", "user")

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ("user_id", "song_id", "rating")
