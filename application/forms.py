from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import ClientUser

class ClientUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = ClientUser
        fields = ('email', 'is_manager', 'client_id')

class ClientUserChangeForm(UserChangeForm):

    class Meta:
        model = ClientUser
        fields = UserChangeForm.Meta.fields
