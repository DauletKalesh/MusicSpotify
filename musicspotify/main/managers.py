from django.db import models
from django.contrib.postgres.aggregates import StringAgg, ArrayAgg
# from django.db.models import 


class TrackManager(models.Manager):

    def get_top_hits(self):
        return self.all().filter(searched_num__gte=100000)
    
    def get_latest(self):
        return self.all().filter(release_date__range=["2021-01-01", "2023-01-31"])

    def get_categories(self):
        return self.values('category')
    
    def grouped_categories(self):
        return self.get_categories().annotate(tracks=StringAgg('track_name', delimiter=', '))

class TrackGenresManager(models.Manager):
    
    def get_genres(self):
        return self.values('genre').annotate(tracks=ArrayAgg('track_name'))

class AlbumManager(models.Manager):

    def get_related(self):
        return self.select_related('artist')
    
    # def 
