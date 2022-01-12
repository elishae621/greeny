from django.views.generic import TemplateView
from django.shortcuts import render 

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
    
    
class ProductDetailView(TemplateView):
    template_name = 'main/product.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Greeny - Product"
        return context
    
class ShopView(TemplateView):
    template_name = 'main/shop.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Greeny - Shop"
        return context
    
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
    