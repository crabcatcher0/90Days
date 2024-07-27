from django.test import SimpleTestCase
from django.urls import reverse, resolve
from api.views import UserView, RegisterView, LoginView

class TestUrls(SimpleTestCase):

    def test_url_user_is_resolved(self):
        url = reverse('profile')
        resolved_view_func = resolve(url).func
        print(resolve(url))
        self.assertEqual(resolved_view_func.view_class, UserView)


    def test_url_register_is_resolved(self):
        url = reverse('register')
        resolved_view_func = resolve(url).func
        print(resolve(url))
        self.assertEqual(resolved_view_func.view_class, RegisterView)


    def test_url_login_is_resolved(self):
        url = reverse('login')
        resolved_view_func = resolve(url).func
        print(resolve(url))
        self.assertEqual(resolved_view_func.view_class, LoginView)
    


    def test_url_profile_id_is_resolved(self):
        url = reverse('profile-detail', args=[5])
        resolved_view_func = resolve(url).func
        print(resolve(url))
        self.assertEqual(resolved_view_func.view_class, UserView)
    