from django.db import models
from django.urls import reverse
# Create your models here.

class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_name = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)

    def __str__(self):
        return self.artist + " - " + self.album_name

    def get_absolute_url(self):
        return reverse('Music:details', kwargs={'pk': self.pk})


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_extension = models.CharField(max_length=20)
    song_name = models.CharField(max_length=100)

    def __str__(self):
        return self.song_name

    def get_absolute_url(self):
        return reverse('Music:details', kwargs={'pk': self.album.pk})
