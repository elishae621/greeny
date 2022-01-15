from django.urls import path 
from . import views 

app_name = 'main'
urlpatterns = [
    path('about/', views.AboutView.as_view(), name='about'),
    path('categories/', views.AllCategoryView.as_view(), name='categories'),
    path('brands/', views.BrandListView.as_view(), name='brands'),
    path('brand/<slug:slug>/', views.BrandSingleView.as_view(), name='brand'),
    path('checkout/', views.CheckoutView.as_view(), name='checkout'),
    path('coming-soon/', views.ComingSoonView.as_view(), name='coming-soon'),
    path('compare/', views.CompareView.as_view(), name='compare'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('faq/', views.FaqView.as_view(), name='faq'),
    path('', views.IndexView.as_view(), name='home'),
    path('invoice/', views.InvoiceView.as_view(), name='invoice'),
    path('offer/', views.OfferView.as_view(), name='offer'),
    path('orders/', views.OrderListView.as_view(), name='orders'),
    path('privacy/', views.PrivacyView.as_view(), name='privacy'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('shop/', views.ShopView.as_view(), name='shop'),
    path('shop/<slug:slug>/', views.ProductDetailView.as_view(), name='product'),
    path('subscribe/', views.SubscribeView.as_view(), name='subscribe'),
    path('wallet/', views.WalletView.as_view(), name='wallet'),
    path('wishlist/', views.WishlistView.as_view(), name='wishlist'),
]