from django.test import TestCase
from django.contrib.auth.forms import UserCreationForm

# Create your tests here.
class UserCreationFormTestCase(TestCase):
    def test_password_too_short(self):
        data = {
            'username': 'kris',
            'password1': 'abc',
            'password2': 'abc'
        }
        form = UserCreationForm(data)
        self.assertFalse(form.is_valid())

    def test_password_too_similar(self):
        data = {
            'username': 'kris',
            'password1': 'kris',
            'password2': 'kris'
        }
        form = UserCreationForm(data)
        self.assertFalse(form.is_valid())

    def test_passwords_dont_match(self):
        data = {
            'username': 'kris',
            'password1': 'goodpass098',
            'password2': 'goodpass099'
        }
        form = UserCreationForm(data)
        self.assertFalse(form.is_valid(), msg="Passwords must match")

    def test_register_successful(self):
        data = {
            'username': 'kris',
            'password1': 'goodpass098',
            'password2': 'goodpass098'
        }
        form = UserCreationForm(data)
        self.assertTrue(form.is_valid())
