# isort:skip_file
from django.urls import include, path
from rest_framework import routers

from .auth.views import RegisterView
from .genres.views import GenreViewSet
from .tracks.views import (
    MostPopularView,
    TrackByGenreView,
    TrackCreateView,
    TrackDetailsView,
    TrackListView,
)

router = routers.DefaultRouter()
router.register(r"genres", GenreViewSet, basename="genres")

urlpatterns = [
    path("tracks/", TrackListView.as_view()),
    path("tracks/<int:id>/", TrackDetailsView.as_view()),
    path("tracks/create/", TrackCreateView.as_view()),
    path("tracks/most_popular/", MostPopularView.as_view()),
    path("tracks/genre/<slug:genre>", TrackByGenreView.as_view()),
    path("auth/register/", RegisterView.as_view(), name="auth_register"),
    path("", include(router.urls)),
]
