from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from rest_auth.serializers import PasswordResetSerializer
from allauth.account.forms import ResetPasswordForm
from . import models

class ClientUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ClientUser
        fields = ('email', 'is_manager', 'client_company_id',)

class ClientUserRegisterSerializer(RegisterSerializer):
    is_manager = serializers.BooleanField(required=True, write_only=True)
    client_company_id = serializers.IntegerField(required=True, write_only=True)

    def get_cleaned_data(self):
        super(ClientUserRegisterSerializer, self).get_cleaned_data()
        return {
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'is_manager': self.validated_data.get('is_manager', ''),
            'client_company_id': self.validated_data.get('client_company_id', '')
        }

class PasswordSerializer (PasswordResetSerializer):
    password_reset_form_class = ResetPasswordForm
