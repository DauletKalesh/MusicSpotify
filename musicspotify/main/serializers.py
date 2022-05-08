from rest_framework import serializers
from main.models import Albums,Artists,Genre,Tracks
from utils.constants import CATEGORY_LIST

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name',)

class TrackGenreSerializer(serializers.Serializer):
    genre = serializers.IntegerField()
    track = serializers.ListField()
    class Meta:
        model = Tracks
        fields = ('genre', 'tracks')

class SimpleTrackSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tracks
        fields = '__all__'

class TrackSerializers(SimpleTrackSerializers):
    genre = GenreSerializer(many = True)
    class Meta:
        model = Tracks
        fields = '__all__'


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artists
        exclude = ('id',)

class AlbumSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer()
    class Meta:
        model = Albums
        fields = ('artist', 'id')
        # fields = '__all__'

class CategorySerializer(serializers.Serializer):
    
    category = serializers.IntegerField()
    tracks = serializers.CharField()
    class Meta:
        fields = ('category', 'tracks')


# class AlbumTrackSerializer(serializers.ModelSerializer):
#     # album = AlbumSerializer(many = False)

#     class Meta:
#         model = Tracks
#         # fields = '__all__'
#         fields = ('id', 'track_name', 'album',)


