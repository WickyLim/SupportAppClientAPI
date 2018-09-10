from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from .models import ClientUser

class ClientUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('is_manager', 'client_company_id')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'is_manager', 'client_company_id', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'client_company_id', 'is_manager', 'is_staff')
    search_fields = ('email', 'client_company_id', 'is_manager')
    ordering = ('email',)

admin.site.register(ClientUser, ClientUserAdmin)
