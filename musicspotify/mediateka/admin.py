from django.contrib import admin
from mediateka.models import Favorite, Playlists

# Register your models here.

# admin.site.register(Favorite)
@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'track')




# admin.site.register(Playlists)
@admin.register(Playlists)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user', 'tracks', 'created_date')

    def tracks(self, obj):
        return ' \n'.join([f'{num+1}) {track}'for num, track in enumerate(obj.track.all())])