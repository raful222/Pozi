from django.contrib.auth.models import User

from django.test import TestCase
from accounts.models import regiter_extra_model


class MyTestCase(TestCase):
    def test_regiter_extra_model(self):
        user1=User.objects.create(username="rafi")
        user = regiter_extra_model.objects.create(user=user1)
        self.assertEquals(str(user), "rafi")
