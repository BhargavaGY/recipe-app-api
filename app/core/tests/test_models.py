"""Testing models"""

from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Test Models"""

    def test_create_user_with_email_successful(self):
        """Test user creation with email is successfull"""

        email = "test@example.com"
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test user email is normalized"""

        sample_emails = [
            ['test1@Example.com', 'test1@example.com'],
            ['Test2@EXAMPLE.com', 'Test2@example.com'],
            ['TEST3@example.COM', 'TEST3@example.com'],
            ['test4@exaMple.COM', 'test4@example.com']
        ]

        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(
                email=email, password='sample123'
                )
            self.assertEqual(user.email, expected)

    def test_new_user_with_no_email_raises_error(self):
        """Test user creation with no email raises ValueError"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', password='test123')

    def test_create_superuser(self):
        """Test create superuser"""
        user = get_user_model().objects.create_superuser(
            email='test1@example.com',
            password='test123'
        )

        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
