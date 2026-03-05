from .views import (RegisterCreateAPI, 
                    LoginView, 
                    LogoutView, 
                    ResetPassword, 
                    OwnProfileView, 
                    ProfileListView, 
                    ProfileDetailView, 
                    AccountListView
)
from django.urls import path


urlpatterns=[
    path('register/', RegisterCreateAPI.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('reset_password/', ResetPassword.as_view(), name='reset_password'),
    path('ownprofile/', OwnProfileView.as_view(), name='own_profile'),
    path('profilelist/', ProfileListView.as_view(), name='profile_list'),
    path('profiledetail/', ProfileDetailView.as_view(), name='profile_dateil'),
    path('accounts/', AccountListView.as_view(), name='accounts')
]