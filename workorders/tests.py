from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from profiles.models import CustomerProfile

class WorkOrderTests(APITestCase):
    def setUp(self):
        user = User.objects.create_user('cust', password='pass')
        self.client.force_authenticate(user)
        self.profile = CustomerProfile.objects.create(user=user)

    def test_create_workorder(self):
        url = reverse('workorder-list')
        data = {
            'customer': self.profile.id,
            'appliance_type': 'Washer',
            'issue_description': 'Not working'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
