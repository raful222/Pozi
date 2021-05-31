from .models import stand_up, sport, motivation
from django import forms


class stand_up_form(forms.ModelForm):
    class Meta:
        model = stand_up
        fields = ('video',)


class sport_form(forms.ModelForm):
    class Meta:
        model = sport
        fields = ('video',)


class motivation_form(forms.ModelForm):
    class Meta:
        model = motivation
        fields = ('video',)
