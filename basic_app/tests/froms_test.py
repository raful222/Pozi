from django.test import TestCase
from basic_app.models import itemReviewToAdmin, stories_model
from basic_app.forms import stories_form, ContactForm


# cl
class Setup_Class(TestCase):

    def setUp(self):
        self.user = itemReviewToAdmin.objects.create(from_email="user@mp.com", subject="user", text="user",
                                                     release_date="1994-20-08")
        self.user = stories_model.objects.create(from_email="user@mp.com", subject="user", text="user")


class User_Form_Test(TestCase):

    def test_ContactForm_valid(self):
        form = ContactForm(
            data={'from_email': "user@mp.com", 'subject': "user", 'text': "user", 'release_date': "1994-20-08"})
        self.assertTrue(form.is_valid())

    def test_ContactForm_invalid(self):
        form = ContactForm(data={'from_email': "", 'subject': "mp", 'text': "mp", 'release_date': ""})
        self.assertFalse(form.is_valid())

    def test_stories_form_valid(self):
        form = stories_form(
            data={'from_email': "user@mp.com", 'subject': "user", 'text': "user"})
        self.assertTrue(form.is_valid())

    def test_stories_form_invalid(self):
        form = stories_form(data={'from_email': "", 'subject': "mp", 'text': "mp"})
        self.assertFalse(form.is_valid())
