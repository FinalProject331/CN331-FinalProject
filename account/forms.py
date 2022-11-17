from django import forms
from django.forms import ModelForm
from .models import Account

class ProfileForm(ModelForm):
    image = forms.ImageField()
    class Meta:
        model = Account
        fields = ['image']
