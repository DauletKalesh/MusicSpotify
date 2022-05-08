from django.urls import path
from main.views import \
    TrackApiView, TrackRetrieveApi, ArtistViewSet,\
        get_top_hits, TrackLatestApiView, get_categories,\
            TrackViewSet, AlbumViewSet #get_tracks
from rest_framework import routers

router = routers.SimpleRouter(trailing_slash=False)
router.register('artists', ArtistViewSet, basename='main')
router.register('tracks', TrackViewSet, basename='main')
router.register('albums', AlbumViewSet, basename='main')

urlpatterns=[
    path('tracks', TrackApiView.as_view()),
    path('tracks/<int:pk>', TrackRetrieveApi.as_view()),
    path('tracks/top_hits', get_top_hits),
    path('tracks/latest', TrackLatestApiView.as_view()),
    path('tracks/categories', get_categories),
    # path('albums/tracks', get_tracks),
] + router.urls