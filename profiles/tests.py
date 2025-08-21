from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse

class ProfileTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user('cust', password='pass')
        self.client.force_authenticate(self.user)

    def test_create_customer_profile(self):
        url = reverse('customerprofile-list')
        data = {
            'user_id': self.user.id,
            'address': '123 St',
            'contact_phone': '555-1234'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
