from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.forms import forms


class regiter_extra_model(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    image = models.ImageField(default='profile_pics/def.jpg', upload_to='profile_pics/', blank=True, null=True)
    date = models.DateField(null=True, blank=True)
    gender = (('male', "Male"), ('female', "Famale"))
    Gender = models.CharField(choices=gender, max_length=300, null=True)

    def __str__(self):
        return str(self.user)


