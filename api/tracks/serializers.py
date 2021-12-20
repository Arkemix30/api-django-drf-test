from rest_framework import serializers

from .models import Track


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = [
            "artistName",
            "name",
            "releaseDate",
            "kind",
            "artistId",
            "artistUrl",
            "contentAdvisoryRating",
            "artworkUrl100",
            "genres",
            "rank",
            "url",
        ]