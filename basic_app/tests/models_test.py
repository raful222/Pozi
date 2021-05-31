from django.test import TestCase
from basic_app.models import itemReviewToAdmin,stories_model


class Test_models(TestCase):
    def test_itemReviewToAdmin(self):
        subject=itemReviewToAdmin.objects.create(subject="this is")
        self.assertEqual(str(subject),"this is")

    def test_stories_model(self):
        subject=stories_model.objects.create(subject="Hello world")
        self.assertEqual(str(subject),"Hello world")