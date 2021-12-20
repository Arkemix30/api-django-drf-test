from rest_framework import permissions, viewsets

from .models import Genre
from .serializers import GenreSerializer


class GenreViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows genre to be viewed or edited.
    """

    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
