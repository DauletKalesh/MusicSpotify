from django.shortcuts import render
from auth_.serializers import \
    UserCreateSerializer, UserSerializer, ProfileSerializer
from rest_framework import generics, mixins, viewsets, status
from rest_framework.decorators import api_view
from rest_framework.views import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from auth_.models import AuthUser, Profile
import logging
logger = logging.getLogger(__name__)

# Create your views here.

class UserViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)
    serializer_class = UserCreateSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.debug("User created")
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_profile(request):
    data = Profile.objects.all().filter(user=request.user)
    serializer = ProfileSerializer(data, many=True)
    logger.debug("Entered profile")
    return Response(serializer.data)