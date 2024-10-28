from datetime import datetime, timedelta

from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from plant_API.models import Plant


class PlantAPIViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.plant = Plant.objects.create(name='Orchid',
                                          species='Orchid',
                                          watering_frequency_days=5,
                                          last_watered_date=datetime.now().date()
                                          )
        self.list_url = reverse('plant-list')
        self.detail_url = reverse('plant-detail', args=[self.plant.id])
        self.watering_url = reverse('plant-watering-plant', args=[self.plant.id])

    def test_plants_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_plants_retrieve(self):
        response = self.client.get(self.detail_url, args=[self.plant.id])
        self.assertEqual(response.data['id'], self.plant.id)
        self.assertEqual(response.data['name'], self.plant.name)
        self.assertEqual(response.data['watering_frequency_days'], self.plant.watering_frequency_days)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_plants_create(self):
        success_data = {
            'name': "Lotus",
            'species': "Lotus",
            'watering_frequency_days': 1,
            'last_watered_date':datetime.now().date()
        }
        wrong_data = {
            'name': "   ",
            'species': "Lotus",
            'watering_frequency_days': '1',
            'last_watered_date':datetime.now().date()
        }
        success_response = self.client.post(self.list_url, data=success_data, format='json')
        self.assertEqual(success_response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(Plant.objects.get(name="Lotus"))

        wrong_response = self.client.post(self.list_url, data=wrong_data, format='json')
        self.assertEqual(wrong_response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_plants_update(self):
        data = {'name': 'Cactus'}
        response = self.client.patch(self.detail_url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.plant.refresh_from_db()
        self.assertEqual(self.plant.name, 'Cactus')

    def test_watering_plant(self):

        response = self.client.patch(self.watering_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


