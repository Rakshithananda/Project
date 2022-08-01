from ast import Mod
from dataclasses import fields
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import ( Revenue_District,
                    Revenue_Mandal,
                    Revenue_Village,
                    Revenue_GSWS,
                    Revenue_VRO,
                    Revenue_VRO_Details,
                    Revenue_Claiment,
                    Schedule_Entry,
                    Register_District,
                    Register_SRO,
                    Register_Village)
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']

# Revenue Forms
class RevenueDistrictForm(ModelForm):
    class Meta:
        model = Revenue_District
        fields = '__all__'

class RevenueMandalForm(ModelForm):
    class Meta:
        model = Revenue_Mandal
        fields = ['district_code','mandal_code','mandal_id','mandal_name']

class RevenueVillageForm(ModelForm):
    class Meta:
        model = Revenue_Village
        fields = ['district_code','mandal_code','village_code','village_id','village_name']

class RevenueGSWSForm(ModelForm):
    class Meta:
        model = Revenue_GSWS
        fields = ['district_code','mandal_code','village_code','gsws_code','gsws_id','gsws_name']

class RevenueVROForm(ModelForm):

    class Meta:
        model = Revenue_VRO
        fields = ['district_code','mandal_code','village_code','gsws_code','vro_code']

class RevenueVRODetailsForm(ModelForm):

    class Meta:
        model = Revenue_VRO_Details
        fields = ['district_code',
                    'mandal_code',
                    'vro_code',
                    'vro_id',
                    'vro_name',
                    'age',
                    'gender',
                    'aadhar',
                    'relation_of',
                    'relation_name',
                    'street',
                    'village_name',
                    'door_no',
                    'pincode',
                    'phone_no']

class RevenueClaimentForm(ModelForm):

    class Meta:
        model = Revenue_Claiment
        fields = ['claiment_id',
                    'gsws_id',
                    'district_code',
                    'mandal_code',
                    'village_code',
                    'gsws_code',
                    'title',
                    'claiment_name',
                    'age',
                    'gender',
                    'aadhar',
                    'relation_of',
                    'relation_name',
                    'village_id',
                    'street',
                    'door_no',
                    'pincode',
                    'phone_no',]

class ScheduleEntryForm(ModelForm):

    class Meta:
        model = Schedule_Entry
        fields = ['claiment_id',
                    'gsws_id',
                    'village_id',
                    'district_code',
                    'mandal_code',
                    'village_code',
                    'gsws_code',
                    'old_house_no',
                    'nature_use',
                    'plot_no',
                    'schedule_no',
                    'jurisdicition',
                    'ward_no',
                    'block_no',
                    'survey_no',
                    'east_eng',
                    'west_eng',
                    'north_eng',
                    'south_eng']

# Register Forms
class RegisterDistrictForm(ModelForm):
    
    class Meta:
        model = Register_District
        fields = '__all__'

class RegisterSROForm(ModelForm):

    class Meta:
        model = Register_SRO
        fields = ['district_code','sro_code','sro_id','sro_name']

class RegisterVillageForm(ModelForm):

    class Meta:
        model = Register_Village
        fields = ['district_code','sro_code','village_code','village_id','village_name']
