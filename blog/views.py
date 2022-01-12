from django.views.generic import TemplateView 


class BlogAuthorView(TemplateView):
    template_name = 'blog/blog-author.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Greeny - Blog Author"
        return context
    
class BlogDetailView(TemplateView):
    template_name = 'blog/blog-details.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Greeny - Blog Details"
        return context
    
class BlogListView(TemplateView):
    template_name = 'blog/blog-standard.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Greeny - Blog Posts"
        return context
    