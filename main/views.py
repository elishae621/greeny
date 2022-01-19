from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http.response import JsonResponse, HttpResponseRedirect
from django.views.generic import TemplateView 
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.http.response import JsonResponse 
from django.urls import reverse
from django.shortcuts import render
from main.models import Category, Faq, Product, Brand, Testimonial, Order, Message
from main.signals import order_created
from user.models import Subscriber, User


def error_404(request, exception):
    data = {}
    return render(request, 'main/error.html', data)

class AboutView(TemplateView):
    template_name = 'main/about.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Greeny - About"
        context["user_count"] = User.objects.count()
        context["product_count"] = Product.objects.count()
        context["testimonials"] = Testimonial.objects.all()[:2]
        return context
    
class AllCategoryView(ListView):
    template_name = 'main/all-category.html'
    model = Category
    context_object_name = 'categories'
    paginate_by = 12
    ordering = ('product_count')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Greeny - All Categories"
        return context
    
    
class BrandListView(ListView):
    template_name = 'main/brand-list.html'
    model = Brand
    context_object_name = 'brands'
    paginate_by = 12
    ordering = ('product_count')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Greeny - Brands"
        return context
    
class BrandSingleView(DetailView):
    template_name = 'main/brand-single.html'
    model = Brand
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titl'e"] = "Greeny - Brand"
        return context
    
class CheckoutView(TemplateView):
    template_name = 'main/checkout.html'
    
    def post(self, request, *args, **kwargs):
        user = request.user
        if user.total_cost != 0:
            order = Order.objects.create(user=user, cost=user.total_cost)
            for item in user.cart.all():
                item.order = order
                item.save()
                order.cart.add(item)
                order.save()
            user.firstname = request.POST.get('firstname')
            user.lastname = request.POST.get('lastname')
            user.city = request.POST.get('city')
            user.phone = request.POST.get('phone')
            user.address = request.POST.get('address')
            user.discount = 0
            if 'apartment' in request.POST:
                user.apartment = request.POST.get('apartment')
            user.email = request.POST.get('email')
            user.save()
            order.city = request.POST.get('city')
            order.phone = request.POST.get('phone')
            if 'apartment' in request.POST:
                order.apartment = request.POST.get('apartment')
            order.email = request.POST.get('email')
            for item in user.cart.all():
                user.cart.remove(item)
            user.save()
            order.address = request.POST.get('address')
            order.state = request.POST.get('state')
            order.country = request.POST.get('country')
            order.notes = request.POST.get('notes')
            order.method = request.POST.get('payment_method')
            order.postcode = request.POST.get('postcode')
            order.save()
            order_created.send(sender=Order, order=order)
            messages.add_message(request, messages.SUCCESS, "Your product will be shipped after payment confirmation, stay in touch")
        return HttpResponseRedirect(reverse('home'))

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

class ContactView(CreateView):
    template_name = 'main/contact.html'
    model = Message
    fields = ['name', 'email', 'subject', 'content']
    
    def get_success_url(self):
        return self.request.path
    
    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, 'Your message has been received. Expect a reply soon.')
        return super().form_valid(form)
        
    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, 'An error occured!')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Greeny - Contact"
        return context
    
class FaqView(ListView):
    template_name = 'main/faq.html'
    model = Faq
    context_object_name = 'faqs'
    
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
        products = Product.objects.all()
        context["featured_products"] = products.filter(featured=True)[:6]
        context["new_products"] = products.order_by("-pub_date")[:5]
        context["top_orders"] = products.order_by("-orders")[:10]
        context["top_rated"] = products.order_by("-rating")[:10]
        context["top_discount"] = products.exclude(discount=0).order_by("-discount")[:10]
        context["brands"] = Brand.objects.all()
        context["testimonials"] = Testimonial.objects.all()
        return context
    
    
class InvoiceView(DetailView):
    template_name = 'main/invoice.html'
    model = Order
    
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
    