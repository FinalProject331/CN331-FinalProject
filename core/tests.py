from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.

# views_test

class AboutusTestCase(TestCase):
    def setup(self):
        self.client = Client()

    def test_views_aboutus(self):

        c = Client()
        response = c.get(reverse('aboutus'))
        self.assertEqual(response.status_code, 200)