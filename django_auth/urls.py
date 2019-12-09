from django.urls import path, include
from allauth.account.views import login, logout

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('login/', login, name="login"),
    path("logout/", logout, name="logout"),
]