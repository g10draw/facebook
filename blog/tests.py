from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your tests here.
class BlogViewsTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home-page')
        self.timeline_url = reverse('timeline-page')
        self.user = get_user_model().objects.create_user(
            username='testuser', password='password')
        self.profile_url = reverse('profile-page', args=[self.user.id])
        self.follow_url = reverse('handle-follow', args=[self.user.id])
        
    def test_home_page_GET(self):
        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/home-page.html')
    
    def test_timeline_page_GET(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(self.timeline_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/timeline.html')
    
    def test_profile_page_GET(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(self.profile_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/profile-page.html')
    
    