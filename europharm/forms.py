from django.contrib.auth.models import User
from django.forms import ModelForm, widgets
from .models import *
from django import forms


class AddProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'title': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.Textarea(attrs={'class': 'form-control'}),
            'author': widgets.TextInput(attrs={'class': 'form-control'}),
            'slug': widgets.TextInput(attrs={'class': 'form-control'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control'})
        }


class AddProductFormUser(ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'created_by', 'title', 'author', 'description', 'image', 'slug', 'price', 'instructions']
        widgets = {
            'title': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.Textarea(attrs={'class': 'form-control'}),
            'author': widgets.TextInput(attrs={'class': 'form-control'}),
            'slug': widgets.TextInput(attrs={'class': 'form-control'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control'})
        }


class AddUserForm(ModelForm):
    username = forms.CharField(max_length=150, required=False)
    first_name = forms.CharField(max_length=150, required=False)
    last_name = forms.CharField(max_length=150, required=False)
    password = forms.PasswordInput()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']


class EditUserForm(ModelForm):
    username = forms.CharField(max_length=150, required=False)
    first_name = forms.CharField(max_length=150, required=False)
    last_name = forms.CharField(max_length=150, required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class EditOrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
