from django.utils import timezone
from django.db import models
from main.models import Tracks
from auth_.models import AuthUser
from django.utils.crypto import get_random_string

# Create your models here.

class Favorite(models.Model):
    track = models.ForeignKey(Tracks, on_delete=models.CASCADE, related_name='favorite')
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE, related_name='user')

    class Meta:
        verbose_name = 'Favorite'
        verbose_name_plural = 'UserFavorites'
        unique_together = (('track', 'user'),)

class Playlists(models.Model):
    name = models.CharField(max_length=50, default=get_random_string(20))
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    track = models.ManyToManyField(Tracks, related_name='playlists')
    created_date = models.DateField(default=timezone.now)

    class Meta:
        verbose_name = 'Playlist'
        verbose_name_plural = 'Playlists'
    
    def __str__(self) -> str:
        return f"{self.name}_{self.user.username}"