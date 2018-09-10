from allauth.account.adapter import DefaultAccountAdapter

class ClientUserAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        from allauth.account.utils import user_field

        user = super().save_user(request, user, form, False)
        user_field(user, 'is_manager', request.data.get('is_manager', ''))
        user_field(user, 'client_company_id', request.data.get('client_company_id', ''))
        user.save()
        return user
