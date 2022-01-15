from django.views.generic import TemplateView 
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.http.response import JsonResponse 
from django.shortcuts import render
from main.models import Category, Product
from user.models import Subscriber 

def error_404(request, exception):
    data = {}
    return render(request, 'main/error.html', data)

class AboutView(TemplateView):
    template_name = 'main/about.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Greeny - About"
        return context
    
class AllCategoryView(TemplateView):
    template_name = 'main/all-category.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Greeny - All Categories"
        return context
    
    
class BrandListView(TemplateView):
    template_name = 'main/brand-list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Greeny - Brands"
        return context
    
class BrandSingleView(TemplateView):
    template_name = 'main/brand-single.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Greeny - Brand"
        return context
    
class CheckoutView(TemplateView):
    template_name = 'main/checkout.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Greeny - checkout"
        return context
    
class ComingSoonView(TemplateView):
    template_name = 'main/coming-soon.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Greeny - Coming Soon"
        return context

class CompareView(TemplateView):
    template_name = 'main/compare.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Greeny - Compare"
        return context

class ContactView(TemplateView):
    template_name = 'main/contact.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Greeny - Contact"
        return context
    
class FaqView(TemplateView):
    template_name = 'main/faq.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Greeny - FAQ"
        return context
    
class IndexView(TemplateView):
    template_name = 'main/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Classic Home - Greeny"
        context["page"] = 'home'
        context['categories'] = Category.objects.all()
        context['products'] = Product.objects.all()
        return context
    
    
class InvoiceView(TemplateView):
    template_name = 'main/invoice.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Greeny - Invoice"
        return context
    
class OfferView(TemplateView):
    template_name = 'main/offer.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Greeny - Promo offer"
        return context
    
class OrderListView(TemplateView):
    template_name = 'main/orderlist.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Greeny - Orders"
        return context
    
class PrivacyView(TemplateView):
    template_name = 'main/privacy.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Privacy Policy"
        context["body_tag_text"] = ' class="scrollspy" data-bs-spy="scroll" data-bs-target="#scrollspy"' 
        return context
    
    
class ProductDetailView(DetailView):
    template_name = 'main/product.html'
    model = Product
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Greeny - Product"
        return context
    
class SearchView(ListView):
    template_name = "main/search.html"
    model = Product
    context_object_name = "products"
    search_fields = ['name']

    def get_queryset(self, **kwargs):
        try:
            key = self.request.GET['key']
            result = list(Product.objects.filter(name__icontains=key)) + list(Product.objects.filter(description__icontains=key)) + list(Product.objects.filter(brand__icontains=key)) + list(Product.objects.filter(tags__icontains=key)) + list(Product.objects.filter(category__icontains=key))
        except KeyError:
            result = Product.objects.all()
        return list(set(result))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        key = self.request.GET.get('key')
        context['search_term'] = key
        context['title'] = f"{key} search results - Your Psychedelic Store"
        return context

class ShopView(TemplateView):
    template_name = 'main/shop.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Greeny - Shop"
        return context
    
class SubscribeView(CreateView):
    model = Subscriber
    
    def form_valid(self, form):
        return JsonResponse({
            'ok': True,
            'message': 'You have been subscribed!'
        })
        
    def form_invalid(self, form):
        return JsonResponse({
            'ok': False,
            'message': 'You are already a subscriber!'
        })
    
class WalletView(TemplateView):
    template_name = 'main/wallet.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Greeny - Wallet"
        return context
    
class WishlistView(TemplateView):
    template_name = 'main/wishlist.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Greeny - Wishlist"
        return context
    