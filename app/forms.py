from django import forms
from django.db import models
from django.forms import fields
from .models import Client, User

class ClientReg(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['client_name','created_by']
        widgets = {
            'client_name': forms.TextInput(attrs={'class':'form-control'}),
            'created_by': forms.TextInput(attrs={'class':'form-control'}),
        }

class UserReg(forms.ModelForm):
    class Meta:
        models = User
        fields = ['user_name','user_password']
        widgets = {
            'user_name': forms.TextInput(attrs={'class':'form-control'}),
            'user_password': forms.TextInput(attrs={'class':'form-control'}),
        }