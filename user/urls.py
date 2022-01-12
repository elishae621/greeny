from django.urls import path 
from . import views 

app_name = 'user'
urlpatterns = [
    path('change-password/', views.ChangePasswordView.as_view(), name='change-password'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('reset-password/', views.ResetPasswordView.as_view(), name='reset-password'),
]