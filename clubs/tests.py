from django.contrib.auth.models import User
from .models import Club
from rest_framework import status
from rest_framework.test import APITestCase


class ClubListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='david', password='pass')

    def test_can_list_clubs(self):
        david = User.objects.get(username='david')
        Club.objects.create(owner=david, name='a name')
        response = self.client.get('/clubs/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_create_club(self):
        self.client.login(username='david', password='pass')
        response = self.client.post('/clubs/', {'name': 'name'})
        count = Club.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
