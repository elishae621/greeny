from django.contrib import admin
from main.models import CartItem, Product, Greeny, Category, Brand, Review, Reply, Variant, Order, Message, Coupon 


@admin.register(Greeny)
class GreenyAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'category', 'brand', 'tags')
    ordering = ('name',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass

@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    pass

@admin.register(Variant)
class VariantAdmin(admin.ModelAdmin):
    pass

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    pass 

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass 

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    pass 

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    pass
