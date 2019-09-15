from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Songs(models.Model):
    title = models.CharField(max_length=255, null=False)
    genre = models.CharField(max_length=255, null=False)
    album = models.CharField(max_length=255, null=False)
    artist = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{} - {} - {} - {}".format(self.title, self.genre, self.album, self.artist)

class Playlist(models.Model):
    name = models.CharField(max_length=200)
    songs = models.ManyToManyField(Songs)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Rating(models.Model):
    SCORE_CHOICES = zip(range(6), range(6) )
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    song_id = models.ForeignKey(Songs, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(choices=SCORE_CHOICES, blank=False)
