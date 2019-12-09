from allauth.account.views import login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, reverse_lazy
from p_library.views import Oauth, RegisterView, CreateUserProfile 
  
app_name = 'p_library'  
urlpatterns = [  
    path('', Oauth.index, name='index'),  
    path('login/', login, name='login'), 
    path('logout/', logout, name='logout'),
    path('register/', RegisterView.as_view(  
        template_name='register.html',  
		success_url=reverse_lazy('p_library:profile-create')  
    ), name='register'),  
    path('profile-create/', CreateUserProfile.as_view(), name='profile-create'),  
]