from django.db import models
from django.urls import reverse
# Create your models here.

class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=250)
    genre = models.CharField(max_length=250)
    logo = models.FileField()

    def __str__(self):
        return self.artist + ' -- ' + self.album_title

    def get_absolute_url(self):
        return reverse('music:detail',kwargs={'pk':self.pk})

class Song(models.Model):
    album = models.ForeignKey(Album,on_delete = models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title=models.CharField(max_length=100)
    is_fav=models.BooleanField(default=False)

    def __str__(self):
        return self.song_title
