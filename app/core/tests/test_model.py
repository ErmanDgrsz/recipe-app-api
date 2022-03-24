from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """test creating a new user with an email as successful"""
        email = "test@email.com"
        password = "testpass123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        # You can't check the password with assertEqual method bc its encrypted.
        # Use check password method
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        email = "test@EMAIL.COM"
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "test123")

    def test_create_new_superuser(self):
        """test of creating a superuser"""
        user = get_user_model().objects.create_superuser(
            "test@email.com",
            "test123"
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
