from django.http import response
from django.test import TestCase, Client 
from django.urls import reverse 


class TestMainLinks(TestCase):
    def setUp(self):
        self.client = Client() 
        
    def test_homepage_works(self):
        response = self.client.get(reverse('main:home'))
        self.assertEqual(response.status_code, 200)
        
    def test_homepage_uses_correct_template(self):
        response = self.client.get(reverse('main:home'))
        self.assertIn('main/index.html', response.template_name)
        
    def test_about_page_works(self):
        response = self.client.get(reverse('main:about'))
        self.assertEqual(response.status_code, 200)
        
    def test_about_page_template(self):
        response = self.client.get(reverse('main:about'))
        self.assertIn('main/about.html', response.template_name)
        
    def test_all_category_page_works(self):
        response = self.client.get(reverse('main:categories'))
        self.assertEqual(response.status_code, 200)
        
    def test_all_category_page_template(self):
        response = self.client.get(reverse('main:categories'))
        self.assertIn('main/all-category.html', response.template_name)
        
    def test_brand_list_page_works(self):
        response = self.client.get(reverse('main:brands'))
        self.assertEqual(response.status_code, 200)
        
    def test_brand_list_page_template(self):
        response = self.client.get(reverse('main:brands'))
        self.assertIn('main/brand-list.html', response.template_name)
        
    def test_brand_single_page_works(self):
        response = self.client.get(reverse('main:brand'))
        self.assertEqual(response.status_code, 200)
        
    def test_brand_single_page_template(self):
        response = self.client.get(reverse('main:brand'))
        self.assertIn('main/brand-single.html', response.template_name)
        
    def test_checkout_page_works(self):
        response = self.client.get(reverse('main:checkout'))
        self.assertEqual(response.status_code, 200)
        
    def test_checkout_page_template(self):
        response = self.client.get(reverse('main:checkout'))
        self.assertIn('main/checkout.html', response.template_name)
    
    def test_coming_soon_page_works(self):
        response = self.client.get(reverse('main:coming-soon'))
        self.assertEqual(response.status_code, 200)
        
    def test_coming_soon_page_template(self):
        response = self.client.get(reverse('main:coming-soon'))
        self.assertIn('main/coming-soon.html', response.template_name)
        
    def test_contact_page_works(self):
        response = self.client.get(reverse('main:contact'))
        self.assertEqual(response.status_code, 200)
        
    def test_contact_page_template(self):
        response = self.client.get(reverse('main:contact'))
        self.assertIn('main/contact.html', response.template_name)
        
    def test_faq_page_works(self):
        response = self.client.get(reverse('main:faq'))
        self.assertEqual(response.status_code, 200)
        
    def test_faq_page_template(self):
        response = self.client.get(reverse('main:faq'))
        self.assertIn('main/faq.html', response.template_name)
        
    def test_invoice_page_works(self):
        response = self.client.get(reverse('main:invoice'))
        self.assertEqual(response.status_code, 200)
        
    def test_invoice_page_template(self):
        response = self.client.get(reverse('main:invoice'))
        self.assertIn('main/invoice.html', response.template_name)

    def test_offer_page_works(self):
        response = self.client.get(reverse('main:offer'))
        self.assertEqual(response.status_code, 200)
        
    def test_offer_page_template(self):
        response = self.client.get(reverse('main:offer'))
        self.assertIn('main/offer.html', response.template_name)
        
    def test_orders_page_works(self):
        response = self.client.get(reverse('main:orders'))
        self.assertEqual(response.status_code, 200)
    
    def test_orders_page_template(self):
        response = self.client.get(reverse('main:orders'))
        self.assertIn('main/orderlist.html', response.template_name)
    
    def test_privacy_page_works(self):
        response = self.client.get(reverse('main:privacy'))
        self.assertEqual(response.status_code, 200)
        
    def test_privacy_page_template(self):
        response = self.client.get(reverse('main:privacy'))
        self.assertIn('main/privacy.html', response.template_name)
        
    def test_product_detail_page_works(self):
        response = self.client.get(reverse('main:product'))
        self.assertEqual(response.status_code, 200)
        
    def test_product_detail_page_template(self):
        response = self.client.get(reverse('main:product'))
        self.assertIn('main/product.html', response.template_name)
        
    def test_shop_page_works(self):
        response = self.client.get(reverse('main:shop'))
        self.assertEqual(response.status_code, 200)
        
    def test_shop_page_template(self):
        response = self.client.get(reverse('main:shop'))
        self.assertIn('main/shop.html', response.template_name)
        
    def test_wallet_page_works(self):
        response = self.client.get(reverse('main:wallet'))
        self.assertEqual(response.status_code, 200)
        
    def test_wallet_page_template(self):
        response = self.client.get(reverse('main:wallet'))
        self.assertIn('main/wallet.html', response.template_name)
        
    def test_wishlist_page_works(self):
        response = self.client.get(reverse('main:wishlist'))
        self.assertEqual(response.status_code, 200)
        
    def test_wishlist_page_template(self):
        response = self.client.get(reverse('main:wishlist'))
        self.assertIn('main/wishlist.html', response.template_name)
        