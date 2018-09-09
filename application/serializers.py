from rest_framework import serializers
from . import models

class ClientUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ClientUser
        fields = ('email', 'is_manager', 'client_company_id',)
