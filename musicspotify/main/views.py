from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.permissions import AllowAny, IsAdminUser
from main.models import Tracks, Artists, Albums, Genre
from main.serializers import TrackSerializers , AlbumSerializer, \
    ArtistSerializer, CategorySerializer, TrackGenreSerializer, SimpleTrackSerializers
        # AlbumTrackSerializer
from rest_framework import viewsets, mixins
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.response import Response
from rest_framework import status
import logging


logger = logging.getLogger(__name__)

# Create your views here.

class TrackApiView(ListAPIView, CreateAPIView):
    queryset = Tracks.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = TrackSerializers

    def post(self, request):
        data = request.data
        self.permission_classes = (IsAdminUser,)
        serializer = SimpleTrackSerializers(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        logger.debug(f"Track is created")
        return Response(serializer.data)


class TrackViewSet(viewsets.ViewSet):
    serializer_class = TrackGenreSerializer

    @action(methods=['GET'], detail=False, permission_classes=(AllowAny,), url_path='genres')
    def get_genres(self, request):
        obj = Tracks.obj_genres.get_genres()
        logger.debug(f"Retrieved Genre object")
        return Response(obj)


class TrackRetrieveApi(RetrieveAPIView):
    queryset = Tracks.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = TrackSerializers

class ArtistViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    queryset = Artists.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [IsAdminUser, ]




@api_view(['GET'])
@permission_classes([AllowAny])
def get_top_hits(request):
    data = Tracks.objects.get_top_hits()
    serializer = TrackSerializers(data, many=True)
    logger.debug("get top hits")
    return Response(serializer.data)

class TrackLatestApiView(ListAPIView):
    queryset = Tracks.objects.get_latest()
    permission_classes = (AllowAny,)
    serializer_class = TrackSerializers


@api_view(['GET'])
@permission_classes([AllowAny])
def get_categories(request):
    data = Tracks.objects.grouped_categories()
    serializer = CategorySerializer(data, many=True)
    logger.debug("get categories")
    return Response(serializer.data)

class AlbumViewSet(mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    permission_classes = (AllowAny,)
    serializer_class = AlbumSerializer
    queryset = Albums.objects.all()


# @api_view(['GET'])
# @permission_classes([AllowAny])
# def get_tracks(request):
#     queryset = Tracks.objects.all()
#     serializer_class = AlbumTrackSerializer
#     serializer = serializer_class(queryset)
#     return Response(serializer.data)

