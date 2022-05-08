from rest_framework import mixins, viewsets, status
from mediateka.models import Favorite, Playlists
from mediateka.serializers import \
    PlaylistSerializer, FavouriteSerializers, CreatePlaylistSerializer,\
        PlaylistDetailSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
import logging

logger = logging.getLogger(__name__)


class PlaylistViewSet(  mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Playlists.objects.all()

    def get_serializer_class(self):
        if self.action in ['list']:
            return PlaylistSerializer
        return CreatePlaylistSerializer
    def get_queryset(self):
        queryset = super().get_queryset()
        if self.action in ['list', 'retrieve']:
            logger.debug("get method playlist")
            return queryset.filter(user=self.request.user.id)
        return queryset

    def create(self, request, *args, **kwargs):
        data = request.data
        data['user'] = self.request.user.id

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def delete(self, request):
        data = request.data
        instance = self.queryset.filter(
            user=self.request.user.id,
            name=data['name']
        )
        instance.delete()
        serializer = PlaylistSerializer(self.queryset.filter(user=request.user.id), many=True)
        return Response(serializer.data)

class PlaylistDetailViewSet(mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Playlists.objects.all()

    def get_serializer_class(self):
        if self.action in ['retrieve']:
            return PlaylistSerializer
        return PlaylistDetailSerializer

    def retrieve(self, request, pk):
        query = self.queryset.filter(id=int(pk), 
                    user=request.user.id)
        if query:
            serializer = PlaylistSerializer(query, many=True)
            return Response(serializer.data)
        return Response({'msg': f'current user does not playlist with id:{pk}'},
                            status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        query = self.queryset.filter(id=int(pk), 
                    user=request.user.id).first()
        data = request.data
        serializer = PlaylistDetailSerializer(instance=query, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        logger.debug(f"Track added to playlist {pk}")

        serializer = PlaylistSerializer(query)
        return Response(serializer.data)
    
    def delete(self, request, pk):
        query = self.queryset.filter(id=int(pk), 
                    user=request.user.id).first()
        data = request.data
        
        query.track.remove(data['track'])
        logger.debug(f"Track deleted from playlist {pk}")

        serializer = PlaylistSerializer(query, many=True)
        return Response(serializer.data)


class FavoriteApiView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        query = Favorite.objects.all().filter(user=request.user.id)
        serializer = FavouriteSerializers(query, many = True)
        logger.debug("get method favorite")
        return Response(serializer.data)
    
    def post(self, request):
        data = request.data
        data['user'] = request.user.id
        serializer = FavouriteSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.debug("added method playlist")
            query = Favorite.objects.all().filter(user=request.user.id)
            serializer = FavouriteSerializers(query, many = True)
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        data = request.data
        data['user'] = request.user.id
        serializer = FavouriteSerializers(data=request.data)
        query = Favorite.objects.all().filter(
            user=request.user.id, track=data['track'])
        query.delete()
        query = Favorite.objects.all().filter(
            user=request.user.id)
        serializer = FavouriteSerializers(query, many = True)
        return Response(serializer.data)