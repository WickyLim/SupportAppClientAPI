from django.urls import include, path
from . import views

urlpatterns = [
    path('client_users/', views.ClientUserListView.as_view()),
    path('auth/', include('rest_auth.urls')),
    path('auth/registration/', include('rest_auth.registration.urls')),
]
