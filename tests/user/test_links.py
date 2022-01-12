from django.http import response
from django.test import TestCase, Client 
from django.urls import reverse 


class TestUserViews(TestCase):
    def setUp(self):
        self.client = Client() 
        
    def test_change_password_page_works(self):
        response = self.client.get(reverse('user:change-password'))
        self.assertEqual(response.status_code, 200)
        
    def test_change_password_page_template(self):
        response = self.client.get(reverse('user:change-password'))
        self.assertIn('user/change-password.html', response.template_name)
    
    def test_login_page_works(self):
        response = self.client.get(reverse('user:login'))
        self.assertEqual(response.status_code, 200)
        
    def test_login_page_template(self):
        response = self.client.get(reverse('user:login'))
        self.assertIn('user/login.html', response.template_name)
        
    def test_profile_page_works(self):
        response = self.client.get(reverse('user:profile'))
        self.assertEqual(response.status_code, 200)
        
    def test_profile_page_template(self):
        response = self.client.get(reverse('user:profile'))
        self.assertIn('user/profile.html', response.template_name)

    def test_register_page_works(self):
        response = self.client.get(reverse('user:register'))
        self.assertEqual(response.status_code, 200)

    def test_register_page_template(self):
        response = self.client.get(reverse('user:register'))
        self.assertIn('user/register.html', response.template_name)

    def test_reset_password_page_works(self):
        response = self.client.get(reverse('user:reset-password'))
        self.assertEqual(response.status_code, 200)
        
    def test_reset_password_page_template(self):
        response = self.client.get(reverse('user:reset-password'))
        self.assertIn('user/reset-password.html', response.template_name)