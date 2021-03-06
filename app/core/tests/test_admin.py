from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email="admin@email.com",
            password="password123"
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email="test@email.com",
            password="password123",
            name="test user full name"
        )

    def test_users_listed(self):
        """test that users are listed in admin page"""
        url = reverse("admin:core_user_changelist")  # This will generate
        # the url for our listed user page
        res = self.client.get(url)  # This will test our client performing get
        # Http request on the url created here

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_page_change(self):
        """test that the user edit page works"""
        url = reverse("admin:core_user_change", args=[self.user.id])
        # admin/core/user/
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """test that create user page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
