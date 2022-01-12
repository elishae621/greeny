from django.views.generic import TemplateView 


class ChangePasswordView(TemplateView):
    template_name = 'user/change-password.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = "user"
        context["title"] = "Greeny - Change Password"
        return context
    
    
class LoginView(TemplateView):
    template_name = 'user/login.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = "user"
        context["title"] = "Greeny - Login"
        return context
    
class ProfileView(TemplateView):
    template_name = 'user/profile.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Greeny - Profile"
        return context
    
    
class RegisterView(TemplateView):
    template_name = 'user/register.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = "user"
        context["title"] = "Greeny - Register"
        return context
    
    
class ResetPasswordView(TemplateView):
    template_name = 'user/reset-password.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = "user"
        context["title"] = "Greeny - Reset Password"
        return context
    