from rest_framework import generics, status
from rest_framework.response import Response

from core.models import User
from core.serializers import UserSerializer

# https://medium.com/@apogiatzis/create-a-restful-api-with-users-and-jwt-authentication-using-django-1-11-drf-part-2-eb6fdcf71f45
class UserViewList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

'''
요청 보내는 법:
import json, requests
data = { ... }
headers = {'Content-Type': 'application/json'}
r = requests.post(url, data=data, headers=headers)
'''