from django.test import TestCase
from chat.models import QA_model, tip_model, chat_first_question_model
from django.contrib.auth.models import User


class Test_models(TestCase):
    def SetUp(self):
        self.user = User.objects.create_user('test', 'test@test.com', 'test')
        self.user.save()
        self.user.chat_first_question_model.taking_medication = "text"
        self.user.chat_first_question_model.Medication_sensitivity = "text1"
        self.user.chat_first_question_model.Corona_feeling = "text2"
        self.user.chat_first_question_model.save()

    def test_QA_model(self):
        subject = QA_model.objects.create(subject="this is")
        self.assertEqual(str(subject), "this is")

    def test_tip_model(self):
        subject = tip_model.objects.create(subject="Hello world")
        self.assertEqual(str(subject), "Hello world")

