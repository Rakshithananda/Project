from dataclasses import fields
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Revenue_District,Revenue_Mandal

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']


class RevenueDistrictForm(ModelForm):
    class Meta:
        model = Revenue_District
        fields = '__all__'

class RevenueMandalForm(ModelForm):
    class Meta:
        model = Revenue_Mandal
        fields = ['mandal_code','dist_code','mandal_id','mandal_name']

# class RevenueVillageForm(ModelForm):
#     class Meta:
#         model = Revenue_Village
#         fields = ['mandal_code','dist_code','village_code','village_id','village_name']