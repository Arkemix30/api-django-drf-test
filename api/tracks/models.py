from django.db import models

from api.genres.models import Genre


class Track(models.Model):
    artistName = models.CharField(max_length=70, blank=False, default="")
    name = models.CharField(max_length=150, blank=False)
    releaseDate = models.DateField(blank=False)
    kind = models.CharField(max_length=20)
    artistId = models.BigIntegerField()
    artistUrl = models.TextField(max_length=255, default="")
    contentAdvisoryRating = models.CharField(max_length=30, null=True)
    artworkUrl100 = models.TextField(max_length=255, default="")
    genres = models.ManyToManyField(Genre, related_name="tracks")
    rank = models.IntegerField(default=0)
    url = models.TextField(max_length=255, default="")

    def __str__(self):
        return self.name
