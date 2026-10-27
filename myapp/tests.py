from django.test import TestCase


class PageViewTests(TestCase):
    def test_home_page(self):
        response = self.client.get("/")

        self.assertContains(response, "Welcome to the Home Page!")

    def test_about_page(self):
        response = self.client.get("/about/")

        self.assertContains(response, "About Page")
