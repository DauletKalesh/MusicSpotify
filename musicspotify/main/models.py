from django.db import models
from utils.validators import validate_track_format, \
    validate_track_size, validate_maximum_time, validate_minimum_time
from utils.constants import CATEGORY_LIST
from utils.upload import *
from main.managers import TrackManager, TrackGenresManager, AlbumManager

class Artists(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, default="", blank=True)
    class Meta:
        verbose_name = 'Artist'
        verbose_name_plural = 'Artists'
    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    


class Genre(models.Model):
    name = models.CharField(max_length=50)
    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'
    
    def __str__(self) -> str:
        return self.name


class Albums(models.Model):
    artist = models.ForeignKey(Artists, on_delete=models.CASCADE, related_name='albums')

    objects = AlbumManager()
    class Meta:
        verbose_name = 'Album'
        verbose_name_plural = 'Albums'
    
    def __str__(self) -> str:
        return f"{self.artist}_album{self.id}"


class Tracks(models.Model):
    track_name =    models.CharField(max_length=255)
    album =         models.ForeignKey(Albums, on_delete=models.CASCADE, related_name='tracks')
    release_date =  models.DateField()
    genre =         models.ManyToManyField(Genre, related_name='tracks')
    category =      models.SmallIntegerField(choices=CATEGORY_LIST, null=True, blank=True)
    searched_num =  models.BigIntegerField(null=True, blank=True)
    duration =      models.TimeField(null=True, blank=True,
        validators=(validate_minimum_time, validate_maximum_time)
    )
    music_doc =     models.FileField(
        upload_to=track_document_path,
        validators=(validate_track_format, validate_track_size)
        )

    objects = TrackManager()
    obj_genres = TrackGenresManager()

    class Meta:
        verbose_name = 'Track'
        verbose_name_plural = 'Tracks'
    
    def __str__(self) -> str:
        return f"{self.track_name}"

# Create your models here.
