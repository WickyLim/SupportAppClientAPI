from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import ClientUserCreationForm, ClientUserChangeForm
from .models import ClientUser

class ClientUserAdmin(UserAdmin):
    add_form = ClientUserCreationForm
    form = ClientUserChangeForm
    model = ClientUser
    list_display = ['email', 'is_manager', 'client_id']

admin.site.register(ClientUser, ClientUserAdmin)
