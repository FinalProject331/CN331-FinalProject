from django import forms
from django.forms import ModelForm
from .models import Shop
from location_field.forms.plain import PlainLocationField


class ProfileShopForm(ModelForm):
    # image = forms.ImageField()
    class Meta:
        model = Shop
        fields = ['shopimg']

        