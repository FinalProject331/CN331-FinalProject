from django import forms
from django.forms import ModelForm
from .models import Shop
from location_field.forms.plain import PlainLocationField

class ShopForm(ModelForm):
    name = forms.CharField(max_length=300)
    detail = forms.CharField(max_length=300)
    shopimg = forms.ImageField()
    location = PlainLocationField(based_fields=['name'])
    
    class Meta:
        model = Shop
        fields = ['name', 'detail', 'shopimg', 'location']



class ProfileShopForm(ModelForm):
    # image = forms.ImageField()
    class Meta:
        model = Shop
        fields = ['shopimg']