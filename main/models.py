from autoslug import AutoSlugField
from decimal import Decimal
from django.core.files import File
from django.db import models
from django.urls import reverse
from django.utils.functional import cached_property
from io import BytesIO
from PIL import Image
from faker import Faker
from django.core.files import File  
import random
import urllib.request
import os 

fake = Faker()
product_url_name = "main:product"



def generate_product_id():
    return random.randint(100000, 1000000)

def generate_price():
    return round(random.random() * 100, 2)

def generate_rating():
    return random.randint(1, 5)

def compress(image):
    img = Image.open(image)
    im_io = BytesIO()
    img.save(im_io, 'png', quality=70)
    img.close()
    new_image = File(im_io, name=image.name)
    return new_image


class Greeny(models.Model):
    delivery = models.IntegerField(default=50) 
    phone = models.CharField(max_length=50, default='(+234) 902 515 9360')
    email = models.EmailField(default='greeny@elishae.me')
    link = models.URLField(default='https://www.elishae.me/')
    owner = models.CharField(max_length=20, default='Surge')

    class Meta:
        verbose_name_plural = "Greeny"

    def __str__(self):
        return 'Greeny'

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='name')

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name 
    
    def get_absolute_url(self):
        return reverse("main:shop") + f'?c={self.slug}'
    

class Brand(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(default="default.jpeg", upload_to="brands/")
    slug = AutoSlugField(populate_from='name')

    def __str__(self):
        return self.name 
    
    def get_absolute_url(self):
        return reverse("main:brand", kwargs={"slug": self.slug})
    

class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    slug = AutoSlugField(populate_from='name', null=True)
    price = models.CharField(max_length=20, default=generate_price)
    image = models.ImageField(default="default.jpeg", upload_to="products/")
    video_url = models.URLField(default='https://www.youtube.com/watch?v=9xzcVxSBbG8&feature=emb_title')
    description = models.TextField(null=True, blank=True, default=fake.paragraph(nb_sentences=5))
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, null=True, on_delete=models.CASCADE)
    no = models.CharField(max_length=10, unique=True, default=generate_product_id)
    tags = models.CharField(max_length=100, null=True, help_text="seperate tags with a comma and single space", default='organic, raw, processed, inorganic')
    pub_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    @cached_property
    def get_tags(self):
        tags = self.tags.split(', ')
        return tags

    def get_absolute_url(self):
        return reverse(product_url_name, kwargs={"slug": self.slug})

class Review(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, default=fake.name())
    content = models.TextField(default=fake.paragraph(nb_sentences=2))
    image = models.ImageField(default="profile.jpeg", upload_to="reviews/")
    date = models.DateTimeField(auto_now_add=True)
    rating = models.PositiveSmallIntegerField(default=generate_rating)
    
    @cached_property
    def star(self):
        stars = []
        for x in range(self.rating):
            stars.append('x')
        return stars

    @cached_property
    def unstar(self):
        stars = []
        for x in range(5 - self.rating):
            stars.append('x')
        return stars
    
    def __str__(self):
        return f'{self.name} on {self.date}' 
    
    def get_absolute_url(self):
        return reverse(product_url_name, kwargs={"slug": self.product.slug}) + f'#review{self.pk}'
    
    
class Reply(models.Model):
    review = models.ForeignKey(Review, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default=fake.name())
    content = models.TextField(default=fake.paragraph(nb_sentences=1))
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Replies'

    def __str__(self):
        return f'{self.name} on {self.date}'
    
    def get_absolute_url(self):
        return reverse(product_url_name, kwargs={"slug": self.review.product.slug}) + f'#reply{self.pk}'

class Variant(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=7, default=generate_price)

    def __str__(self):
        return f"{self.name} - {self.price}"

    def get_absolute_url(self):
        return reverse(product_url_name, kwargs={"slug": self.product.slug})

class CartItem(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    cart_order = models.ForeignKey(
        'main.Order', null=True, on_delete=models.CASCADE)
    cost = models.DecimalField(decimal_places=2, max_digits=7, default=0.00)
    owner = models.ForeignKey(
        'user.User', on_delete=models.CASCADE, null=True)
    variant = models.ForeignKey(Variant, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product.name}'

    def save(self, *args, **kwargs):
        self.cost = self.variant.price * Decimal(self.quantity)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("main:home") + '#cart'
    

class OrderStatus(models.TextChoices):
    CREATED = 'CREATED'
    IN_PROGRESS = 'IN PROGRESS'
    DELIVERED = 'DELIVERED'
    CANCELLED = 'CANCELLED'


class Order(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    address = models.CharField(
        max_length=50, default='', null=True, blank=True)
    apartment = models.CharField(
        max_length=30, default='', null=True, blank=True)
    city = models.CharField(max_length=20, default='', null=True, blank=True)
    state = models.CharField(max_length=30, default='', null=True, blank=True)
    country = models.CharField(max_length=50, default='', null=True, blank=True)
    phone = models.CharField(max_length=15, default='', null=True, blank=True)
    email = models.EmailField(default='', null=True, blank=True)
    cart = models.ManyToManyField(CartItem)
    products = models.TextField(null=True, blank=True, default='')
    cost = models.IntegerField(default=0)
    notes = models.TextField(null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=11, choices=OrderStatus.choices, default=OrderStatus.CREATED)
    method = models.CharField(max_length=50, default='', null=True)

    @cached_property
    def get_products(self):
        self.products = ''
        for idx, item in enumerate(list(self.user.cart.all())):
            self.products += f'({idx+1}) {item.product.name} {item.variant} at {item.variant.price} \n\n'
        return self.products

    def save(self, *args, **kwargs):
        if self.id:
            self.products = self.get_products
            total_cost = 0
            for item in self.cart.all():
                total_cost += item.variant.price
            self.total_cost = total_cost
        super().save(*args, **kwargs)

    def __str__(self):
        return f'order by {self.user.firstname}'


class MessageStatus(models.TextChoices):
    NEW = 'NEW'
    WAITING = 'WAITING'
    FINISHED = 'FINISHED'


class Message(models.Model):
    name = models.CharField(max_length=40, null=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=15, null=True)
    content = models.TextField(null=True)
    date_sent = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=15, choices=MessageStatus.choices, default=MessageStatus.NEW)

    def __str__(self):
        return f'{self.name} on {self.date_sent}'


class Coupon(models.Model):
    code = models.CharField(max_length=30)
    discount = models.IntegerField(default=10)