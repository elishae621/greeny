from django.views.generic import TemplateView 


class ChangePasswordView(TemplateView):
    template_name = 'user/change-password.html'
    
class LoginView(TemplateView):
    template_name = 'user/login.html'
    
class ProfileView(TemplateView):
    template_name = 'user/profile.html'
    
class RegisterView(TemplateView):
    template_name = 'user/register.html'
    
class ResetPasswordView(TemplateView):
    template_name = 'user/reset-password.html'