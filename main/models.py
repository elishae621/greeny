from email.policy import default
from autoslug import AutoSlugField
from decimal import Decimal
from django.core.exceptions import ValidationError
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
default_profile_image = "profile.jpg"
default_image = "default.png"


def generate_product_id():
    return random.randint(100000, 1000000)

def generate_old_price():
    return round(random.random() * 100 + 20, 2)

def generate_price():
    return round(random.random() * 100, 2)

def generate_order():
    return random.randint(0, 100)

def generate_rating():
    return random.randint(1, 5)

def generate_discount():
    return fake.random_element(elements=[0, 0, 10, 20])

def generate_rating_count():
    return random.randint(12, 54)

def generate_testi_title():
    return f"{fake.random_element(elements=['Former MD', 'MD'])} - {fake.company()}"

def generate_product_description():
    return fake.paragraph(nb_sentences=5)

def generate_comment_content():
    return fake.paragraph(nb_sentences=1)

def generate_name():
    return fake.name()

def generate_testi_rating():
    return random.randint(4, 5)

def generate_team_title():
    n = 1
    if n == 1:
        yield 'Founder & CEO'
    n += 1
    if n == 2:
        yield 'Web developer'
    n += 1 
    if n == 3:
        yield 'Digital Marketer'
    n += 1
    if n == 4:
        n = 1
        yield 'Article Writer'

def compress(image):
    img = Image.open(image)
    im_io = BytesIO()
    img.save(im_io, 'png', quality=70)
    img.close()
    new_image = File(im_io, name=image.name)
    return new_image

def list_rating(rating):
    final = ""
    for n in range(rating):
        final += 'x'
    return final

def validate_rating(value):
    if value < 1 or value > 5:
        raise ValidationError('%(value)s is not between 1 and 5',
        params={'value': value},
        )

class Greeny(models.Model):
    delivery = models.IntegerField(default=50) 
    phone = models.CharField(max_length=50, default='(+234) 902 515 9360')
    email = models.EmailField(default='greeny@elishae.me')
    address = models.CharField(max_length=200, default='1Hd- 50, 010 Avenue, NY 90001 United States')
    link = models.URLField(default='https://elishae.me/')
    owner = models.CharField(max_length=20, default='Surge')
    facebook = models.URLField(default='https://facebook.com')
    twitter = models.URLField(default='https://twitter.com')
    linkedin = models.URLField(default='https://linkedIn.com')
    instagram = models.URLField(default='https://instagram.com')
    interest = models.URLField(default='https://pinterest.com')


    class Meta:
        verbose_name_plural = "Greeny"

    def __str__(self):
        return 'Greeny'

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='name')
    image = models.ImageField(default=default_image, upload_to="categories/")
    product_count = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name 
    
    def get_absolute_url(self):
        return reverse("main:shop") + f'?c={self.slug}'
    
    def save(self, *args, **kwargs):
        new_image = compress(self.image)
        self.image = new_image
        self.product_count = self.product_set.count()
        return super().save(*args, **kwargs)
    

class Brand(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(default=default_image, upload_to="brands/")
    slug = AutoSlugField(populate_from='name')
    product_count = models.IntegerField(default=0)
    rating_count = models.IntegerField(default=generate_rating_count)

    def __str__(self):
        return self.name 
    
    def save(self, *args, **kwargs):
        new_image = compress(self.image)
        self.image = new_image
        self.product_count = self.product_set.count()
        return super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("main:brand", kwargs={"slug": self.slug})
    
class LabelColor(models.TextChoices):
    green = 'new'
    grey = 'stockout'
    blue = 'stockblue'
    red = 'sale'

class ProductAvaliability(models.TextChoices):
    stock_in = 'stock in'
    stock_out = 'stock out'

class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    slug = AutoSlugField(populate_from='name', null=True)
    old_price = models.CharField(max_length=20, default=generate_old_price)
    price = models.CharField(max_length=20, default=generate_price)
    image = models.ImageField(default=default_image, upload_to="products/")
    video_url = models.URLField(default='https://www.youtube.com/watch?v=9xzcVxSBbG8&feature=emb_title')
    description = models.TextField(null=True, blank=True, default=generate_product_description)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, null=True, on_delete=models.CASCADE)
    no = models.CharField(max_length=10, unique=True, default=generate_product_id)
    tags = models.CharField(max_length=100, null=True, help_text="seperate tags with a comma and single space", default='organic, raw, processed, inorganic')
    pub_date = models.DateField(auto_now_add=True)
    label = models.CharField(max_length=20, null=True, blank=True)
    labelColor = models.CharField(max_length=10, choices=LabelColor.choices, null=True, blank=True)
    labelClass = models.CharField(max_length=5, null=True, blank=True)
    rating = models.PositiveSmallIntegerField(default=generate_rating, validators=[validate_rating])
    featured = models.BooleanField(default=False)
    orders = models.IntegerField(default=generate_order)
    discount = models.IntegerField(default=generate_discount)
    status = models.CharField(max_length=9, choices=ProductAvaliability.choices, default=ProductAvaliability.stock_in)
   
    def __str__(self):
        return self.name
    
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
    
    def save(self, *args, **kwargs):
        new_image = compress(self.image)
        self.image = new_image
        if self.label:
            self.label = self.label.upper()
            if self.labelColor.lower() == 'green':
                self.labelClass = 'new'
            elif self.labelColor.lower() == 'grey':
                self.labelClass = 'stockout'
            elif self.labelColor.lower() == 'blue':
                self.labelClass = 'stockblue'
            elif self.labelColor.lower() == 'red':
                self.labelClass = 'sale'
        return super().save(*args, **kwargs)
    
    @cached_property
    def get_tags(self):
        tags = self.tags.split(', ')
        return tags

    def get_absolute_url(self):
        return reverse(product_url_name, kwargs={"slug": self.slug})

class Review(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, default=generate_name)
    content = models.TextField(default=generate_comment_content)
    image = models.ImageField(default=default_profile_image, upload_to="reviews/")
    date = models.DateTimeField(auto_now_add=True)
    rating = models.PositiveSmallIntegerField(default=generate_rating, validators=[validate_rating])
    
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
    
    def save(self, *args, **kwargs):
        new_image = compress(self.image)
        self.image = new_image
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return f'{self.name} on {self.date}' 
    
    def get_absolute_url(self):
        return reverse(product_url_name, kwargs={"slug": self.product.slug}) + f'#review{self.pk}'
    
    
class Reply(models.Model):
    review = models.ForeignKey(Review, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default=generate_name)
    content = models.TextField(default=generate_comment_content)
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
    no = models.CharField(max_length=15, default=generate_product_id)
    slug = AutoSlugField(populate_from='no', null=True)
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
    method = models.CharField(max_length=50, default='card payment', null=True)
    cost = models.DecimalField(decimal_places=2, max_digits=7, default=0.00)
    discount = models.DecimalField(decimal_places=2, max_digits=7, default=0.00)
    delivery = models.DecimalField(decimal_places=2, max_digits=7, default=0.00)
    notes = models.TextField(null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=11, choices=OrderStatus.choices, default=OrderStatus.CREATED)
    method = models.CharField(max_length=50, default='card payment', null=True)
    delivery_time = models.CharField(max_length=50, default='90 minutes express delivery', null=True)

    @cached_property
    def get_products(self):
        self.products = ''
        for idx, item in enumerate(list(self.cart.all())):
            self.products += f'({idx+1}) {item.product.name} {item.variant} at {item.variant.price} \n\n'
        return self.products

    def subtotal(self):
        total = 0
        for item in self.cart.all():
            total += (item.product.price * item.quantity)
        return total
        
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
    subject = models.CharField(max_length=225, null=True)
    content = models.TextField(null=True)
    date_sent = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=15, choices=MessageStatus.choices, default=MessageStatus.NEW)

    def __str__(self):
        return f'{self.name} on {self.date_sent}'


class Coupon(models.Model):
    code = models.CharField(max_length=30)
    discount = models.IntegerField(default=10)
    link = models.URLField(default='/')
    

class Testimonial(models.Model):
    name = models.CharField(max_length=20, default=generate_name)
    title = models.CharField(max_length=50, default=generate_testi_title)
    content = models.TextField(default=generate_comment_content)
    rating = models.IntegerField(validators=[validate_rating], default=generate_testi_rating)
    image = models.ImageField(default=default_profile_image, upload_to="testimonials/")
    
    
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
    
    def save(self, *args, **kwargs):
        new_image = compress(self.image)
        self.image = new_image
        return super().save(*args, **kwargs)
    
class TeamMember(models.Model):
    name = models.CharField(max_length=20, default=generate_name)
    title = models.CharField(max_length=50, default=generate_team_title)
    image = models.ImageField(default=default_profile_image, upload_to="team_members/")
    facebook = models.URLField(default='https://facebook.com')
    twitter = models.URLField(default='https://twitter.com')
    linkedin = models.URLField(default='https://linkedIn.com')
    
class Faq(models.Model):
    question = models.TextField()
    answer = models.TextField()
    
    def str(self):
        return self.question[:20]
    