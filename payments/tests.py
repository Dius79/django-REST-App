from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse

class PaymentTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user('payuser', password='pass')
        self.client.force_authenticate(self.user)

    def test_create_intent(self):
        url = reverse('stripe-intent')
        response = self.client.post(url, {'amount': 1000, 'currency': 'usd'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('client_secret', response.data)
