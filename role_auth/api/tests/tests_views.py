from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from api.models import CustomUser


class RegisterViewTest(TestCase):

    def setup(self):
        self.client = APIClient()
        self.User = CustomUser()
    

    def test_register_user_success(self):
        url = '/api/register'  
        data = {
            'email': 'newuser@example.com',
            'password': 'securepassword',
            'first_name': 'Jane',
            'last_name': 'Doe'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(CustomUser.objects.filter(email=data['email']).exists())
        self.assertEqual(response.data['email'], data['email'])
        self.assertEqual(response.data['first_name'], data['first_name'])
        self.assertEqual(response.data['last_name'], data['last_name'])


    def test_register_user_failure(self):
        url = '/api/register'  
        data = {
            'email': 'ram@short_format',  
            'password': 'short',
            'first_name': '',
            'last_name': '',  
        }
        response = self.client.post(url, data, format='json')
        response_data = response.data
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response_data)
        self.assertIn('Enter a valid email address.', response_data['email'][0])
        self.assertIn('password', response_data)
        self.assertIn('Ensure this field has at least 8 characters.', response_data['password'][0])
        self.assertIn('first_name', response_data)
        self.assertIn('This field may not be blank.', response_data['first_name'][0])
        self.assertIn('last_name', response_data)
        self.assertIn('This field may not be blank.', response_data['last_name'][0])




class LoginViewTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(
            email='testuser@example.com',
            password='securepassword',
            first_name='ram',
            last_name='nai'
        )


    # def test_login_success(self):
    #     url = '/api/login'  
    #     data = {
    #         'email': 'ram@gmail.com',
    #         'password': '####'
    #     }
    #     response = self.client.post(url, data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertIn('access', response.data)
    #     self.assertIn('refresh', response.data)



    def test_login_failure(self):
        url = '/api/login'
        data = {
            'email': 'ram@gmail.com',
            'password': 'wrongpassword'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn('detail', response.data)
        self.assertEqual(response.data['detail'], 'No active account found with the given credentials')


    def test_login_missing_fields(self):
        url = '/api/login'  
        data = {
            'email': 'ram@gmail.com'
            #no pass
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('password', response.data)
        self.assertEqual(response.data['password'][0], 'This field is required.')