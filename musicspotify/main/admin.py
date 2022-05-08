from django.contrib import admin
from main.models import Tracks, Artists, Genre, Albums

# Register your models here.
# admin.site.register(Tracks)
@admin.register(Tracks)
class TrackAdmin(admin.ModelAdmin):
    list_display = ('id', 'track_name', 'release_date', 'album',
            'get_products', 'category', 'searched_num', 'duration', 'music_doc')
    
    def get_products(self, obj):
        return " \n".join([p.name for p in obj.genre.all()])


admin.site.register(Artists)
admin.site.register(Genre)
admin.site.register(Albums)