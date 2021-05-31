from django.test import TestCase
from django.urls import reverse, resolve
from basic_app.views import stories, consultation, index, font_changing, Videos, about, Review, detail, edit_story, \
    delete_story


class TestUrls(TestCase):
    def test_stories(self):
        url = reverse('basic_app:stories')
        # print(resolve(url))
        self.assertEqual(resolve(url).func, stories)

    def test_consultation(self):
        url = reverse('basic_app:consultation')
        self.assertEqual(resolve(url).func, consultation)

    def test_index(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func, index)

    def test_font_changing(self):
        url = reverse('basic_app:font_changing')
        self.assertEqual(resolve(url).func, font_changing)

    def test_Videos(self):
        url = reverse('basic_app:Videos')
        self.assertEqual(resolve(url).func, Videos)

    def test_about(self):
        url = reverse('basic_app:about')
        self.assertEqual(resolve(url).func, about)

    def test_Review(self):
        url = reverse('basic_app:Review')
        self.assertEqual(resolve(url).func, Review)
