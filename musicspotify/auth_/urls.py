from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from auth_.views import UserViewSet, get_profile

urlpatterns=[
    path('login', obtain_jwt_token),
    path('registration', UserViewSet.as_view({'post':'create'})),
    path('profile', get_profile)
]