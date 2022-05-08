from django.urls import path
from mediateka.views import FavoriteApiView, PlaylistViewSet, PlaylistDetailViewSet
from rest_framework.routers import SimpleRouter
from rest_framework import routers

router = routers.SimpleRouter(trailing_slash=False)
router.register('playlist', PlaylistViewSet, basename='mediateka')
playlist_detail = PlaylistDetailViewSet.as_view({
    'get':'retrieve',
    'put': 'update',
})


urlpatterns = [
    path('favorite', FavoriteApiView.as_view()),
    path('playlist/<int:pk>', playlist_detail)
] + router.urls
