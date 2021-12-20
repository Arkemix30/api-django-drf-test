from django.core.cache import cache
from rest_framework import generics, permissions

from .models import Track
from .serializers import TrackSerializer


class TrackListView(generics.ListAPIView):

    serializer_class = TrackSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        """
        This view should return a list of all the tracks
        as determined by the name portion of the URL.
        """
        queryset = Track.objects.all()

        if self.request.query_params.get("name"):
            name = self.request.query_params.get("name")
            sql_query = """
            SELECT * FROM api_track
            WHERE name LIKE '%{}%'
            """.format(
                name
            )
            if name:
                queryset = Track.objects.raw(sql_query)

        # Filtering by artistName
        if self.request.query_params.get("artistName"):
            artistName = self.request.query_params.get("artistName")
            sql_query = """
            SELECT * FROM api_track
            WHERE artistName LIKE '%{}%'
            """.format(
                artistName
            )
            if artistName:
                queryset = Track.objects.raw(sql_query)
        return queryset


class TrackDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """
    This view should retrieve, update and destroy (CRUD)
    by given ID
    """

    lookup_field = "id"
    queryset = Track.objects.all()
    serializer_class = TrackSerializer


class TrackCreateView(generics.CreateAPIView):
    """
    This view should create a Track and insert it into
    the database
    """

    queryset = Track.objects.all()
    serializer_class = TrackSerializer


class MostPopularView(generics.ListAPIView):
    """
    This view should return a list
    50 tracks ordered by popularity rank
    """

    serializer_class = TrackSerializer

    def get_queryset(self):
        queryset = Track.objects.raw(
            """
        SELECT * FROM api_track
        ORDER BY rank ASC
        LIMIT 50"""
        )
        return queryset


class TrackByGenreView(generics.ListAPIView):
    serializer_class = TrackSerializer

    def get_queryset(self):
        """
        This view should return a list of all tracks
        filtered by a given genre name
        """
        queryset = Track.objects.all()
        if self.kwargs["genre"]:
            genre = self.kwargs["genre"]
            if genre:
                queryset = Track.objects.filter(genres__name=genre)
        return queryset
