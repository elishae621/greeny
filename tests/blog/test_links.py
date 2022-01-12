from django.http import response
from django.test import TestCase, Client 
from django.urls import reverse 


class TestBlogView(TestCase):
    def setUp(self):
        self.client = Client() 
        
    def test_blog_author_view_page_works(self):
        response = self.client.get(reverse('blog:author'))
        self.assertEqual(response.status_code, 200)
        
    def test_blog_author_view_page_template(self):
        response = self.client.get(reverse('blog:author'))
        self.assertIn('blog/blog-author.html', response.template_name)
        
    def test_blog_detail_view_page_works(self):
        response = self.client.get(reverse('blog:detail'))
        self.assertEqual(response.status_code, 200)
        
    def test_blog_detail_view_page_template(self):
        response = self.client.get(reverse('blog:detail'))
        self.assertIn('blog/blog-details.html', response.template_name)
        
    def test_blog_list_view_page_works(self):
        response = self.client.get(reverse('blog:list'))
        self.assertEqual(response.status_code, 200)
        
    def test_blog_list_view_page_template(self):
        response = self.client.get(reverse('blog:list'))
        self.assertIn('blog/blog-standard.html', response.template_name)
