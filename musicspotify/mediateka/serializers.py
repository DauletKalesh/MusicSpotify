from pyexpat import model
from rest_framework import serializers
from mediateka.models import Favorite, Playlists
from main.models import Tracks
from main.serializers import TrackSerializers

class FavouriteSerializers(serializers.ModelSerializer):
    
    # user = serializers.IntegerField()
    # track = serializers.IntegerField()
    class Meta:
        model = Favorite
        fields =  ('user', 'track')

class PlaylistSerializer(FavouriteSerializers):
    track = TrackSerializers(many=True)
    class Meta:
        model = Playlists
        fields = ('name', 'user', 'track')

class CreatePlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlists
        fields = ('name', 'user')

class PlaylistDetailSerializer(serializers.Serializer):
    track = serializers.IntegerField()
    class Meta:
        model = Playlists
        fields = ('track')
    
    def update(self, instance, validated_data):
        instance.track.add(int(validated_data['track']))
        return instance


