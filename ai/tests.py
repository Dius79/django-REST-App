from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse

class AITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user('user', password='pass')
        self.client.force_authenticate(self.user)

    def test_diagnosis(self):
        url = reverse('diagnosis')
        data = {
            'appliance_type': 'Dryer',
            'issue_description': 'Makes noise'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('suggestion', response.data)
