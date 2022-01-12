from django.urls import path
from . import views 

urlpatterns = [
    path('author/', views.BlogAuthorView.as_view(), name='author'),
    path('detail/', views.BlogDetailView.as_view(), name='detail'),
    path('list/', views.BlogListView.as_view(), name='list'),
]