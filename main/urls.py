from django.urls import path 
from . import views 

app_name = 'main'
urlpatterns = [
    path('about/', views.AboutView.as_view(), name='about'),
    path('all-category/', views.AllCategoryView.as_view(), name='category'),
    path('brand/list/', views.BrandListView.as_view(), name='brand-list'),
    path('brand/single/', views.BrandSingleView.as_view(), name='brand-single'),
    path('checkout/', views.CheckoutView.as_view(), name='checkout'),
    path('coming-soon/', views.ComingSoonView.as_view(), name='coming-soon'),
    path('faq/', views.FaqView.as_view(), name='faq'),
    path('', views.IndexView.as_view(), name='home'),
    path('invoice/', views.InvoiceView.as_view(), name='invoice'),
    path('offer/', views.OfferView.as_view(), name='offer'),
    path('orders/', views.OrderListView.as_view(), name='orders'),
    path('privacy/', views.PrivacyView.as_view(), name='privacy'),
    path('product/detail/', views.ProductDetailView.as_view(), name='product'),
    path('shop/', views.ShopView.as_view(), name='shop'),
    path('wallet/', views.WalletView.as_view(), name='wallet'),
    path('wishlist/', views.WishlistView.as_view(), name='wishlist'),
]