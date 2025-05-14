from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status


class InfoViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('info')

    def test_get_info(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'Hello its Ashok!') 