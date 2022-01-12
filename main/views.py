from django.views.generic import TemplateView
from django.shortcuts import render 

def error_404(request, exception):
    data = {}
    return render(request, 'main/error.html', data)

class AboutView(TemplateView):
    template_name = 'main/about.html'
    
class AllCategoryView(TemplateView):
    template_name = 'main/all-category.html'
    
class BrandListView(TemplateView):
    template_name = 'main/brand-list.html'
    
class BrandSingleView(TemplateView):
    template_name = 'main/brand-single.html'
    
class CheckoutView(TemplateView):
    template_name = 'main/checkout.html'
    
class ComingSoonView(TemplateView):
    template_name = 'main/coming-soon.html'
    
class FaqView(TemplateView):
    template_name = 'main/faq.html'
    
class IndexView(TemplateView):
    template_name = 'main/index.html'
    
class InvoiceView(TemplateView):
    template_name = 'main/invoice.html'
    
class OfferView(TemplateView):
    template_name = 'main/offer.html'
    
class OrderListView(TemplateView):
    template_name = 'main/orderlist.html'
    
class PrivacyView(TemplateView):
    template_name = 'main/privacy.html'
    
class ProductDetailView(TemplateView):
    template_name = 'main/product.html'
    
class ShopView(TemplateView):
    template_name = 'main/shop.html'
    
class WalletView(TemplateView):
    template_name = 'main/wallet.html'
    
class WishlistView(TemplateView):
    template_name = 'main/wishlist.html'