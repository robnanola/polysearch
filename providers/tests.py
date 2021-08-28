"""
Provider related tests
"""
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from .models import Provider


class ProviderTestCase(APITestCase):
    """
    Test cases for Provider creation and phone validation.
    """
    def setUp(self):
        """
        Setup initial providers
        """
        data = [
            {"name": "Test Provider",
            "email": "user@test.com",
            "phone_number": "+639178872255",
            "language": "EN",
            "currency": "PHP"},
            {"name": "Test Provider 2",
            "email": "user2@test.com",
            "phone_number": "+639771166005",
            "language": "EN",
            "currency": "PHP"},
        ]
        for provider in data:
            Provider.objects.create(**provider)

    def test_viewset_get(self):
        """
        Test provider list GET
        """
        response = self.client.get(reverse("provider-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 2)

    def test_viewset_phone_validation(self):
        """
        Test cases for phone_number validations
        """
        data = {
            "name": "Provider1",
            "email": "user@provider.com",
            "phone_number": "917-887-2255",
            "language": "EN",
            "currency": "PHP"
        }

        response = self.client.post(reverse("provider-list"), data, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['phone_number'][0], 'Invalid format. ei: +999999999')

        data['phone_number'] = '++639172223345'
        response = self.client.post(reverse("provider-list"), data, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['phone_number'][0], 'Invalid format. ei: +999999999')

        data['phone_number'] = '6391722'
        response = self.client.post(reverse("provider-list"), data, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['phone_number'][0], 'Invalid format. ei: +999999999')

        data['phone_number'] = 'acbcehdfgh'
        response = self.client.post(reverse("provider-list"), data, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['phone_number'][0], 'Invalid format. ei: +999999999')
