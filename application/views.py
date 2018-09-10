from rest_framework import generics

from . import models
from . import serializers

class ClientUserListView(generics.ListCreateAPIView):
    queryset = models.ClientUser.objects.all()
    serializer_class = serializers.ClientUserSerializer
