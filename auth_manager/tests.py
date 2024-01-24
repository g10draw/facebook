from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your tests here.
class AuthViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register-page')
        self.login_url = reverse('login-page')
        self.logout_url = reverse('logout-page')
        self.user = get_user_model().objects.create(username='testuser', password='password')
    
    def test_user_registration_POST(self):
        response = self.client.post(self.register_url, {
            'username': 'testuser2',
            'password1': 'testpass123',
            'password2': 'testpass123'
        })

        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, reverse('login-page'))
    
    def test_user_login_POST(self):
        self.client.login(username='testuser', password='password')

        response = self.client.post(self.login_url, {
            'username': 'testuser',
            'password': 'password'
        })

        self.assertEquals(response.status_code, 200)
        # self.assertRedirects(response, reverse('timeline-page'))
    
    def test_user_logout_GET(self):
        self.client.login(username='testuser', password='password')

        response = self.client.get(self.logout_url)

        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, reverse('home-page'))