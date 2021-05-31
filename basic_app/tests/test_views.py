from django.test import TestCase, Client
from basic_app.views import index, Review, about, Videos, font_changing, stories, consultation, detail
from django.contrib.auth.models import User
from django.urls import reverse
from basic_app.models import itemReviewToAdmin, stories_model
import json


class Test_views(TestCase):

    def test_Review(self):
        self.client = Client()
        response = self.client.get(reverse('basic_app:Review'))
        self.assertEqual(response.status_code, 200)

    def test_about(self):
        self.client = Client()
        response = self.client.get(reverse('basic_app:about'))
        self.assertEqual(response.status_code, 200)

    def test_Videos(self):
        self.client = Client()
        response = self.client.get(reverse('basic_app:Videos'))
        self.assertEqual(response.status_code, 200)

    def test_font_changing(self):
        self.client = Client()
        response = self.client.get(reverse('basic_app:font_changing'))
        self.assertEqual(response.status_code, 200)

    def test_stories(self):
        self.client = Client()
        response = self.client.get(reverse('basic_app:stories'))
        self.assertEqual(response.status_code, 200)

    def test_consultation(self):
        self.client = Client()
        response = self.client.get(reverse('basic_app:consultation'))
        self.assertEqual(response.status_code, 200)