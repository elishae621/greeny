from django.views.generic import TemplateView 


class BlogAuthorView(TemplateView):
    template_name = 'blog/blog-author.html'
    
class BlogDetailView(TemplateView):
    template_name = 'blog/blog-details.html'
    
class BlogListView(TemplateView):
    template_name = 'blog/blog-standard.html'