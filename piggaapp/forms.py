from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Permission, Group
from django import forms
from django.contrib.auth.forms import AuthenticationForm


class AddUserForm(UserCreationForm):
    superuser = forms.BooleanField(required=False)
    staff = forms.BooleanField(required=False)
    customer = forms.BooleanField(required=False)
    address = forms.CharField(max_length=200, required=True)
    email = forms.EmailField(required=True, max_length=200)
    phonenumber = forms.CharField(required=True, max_length=200)
    
    class Meta:
        model = User
        fields = ["username", "email", "address", "phonenumber", "password1", "password2", "is_superuser", "is_staff"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            UserProfile.objects.create(user=user, address=self.cleaned_data['address'])
            user.user_permissions.set(self.cleaned_data['user_permissions'])
        return user    
        
class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"


class RegisterForm(UserCreationForm):
    address = forms.CharField(max_length=200, required=True)
    email = forms.EmailField(required=True, max_length=200)
    phonenumber = forms.CharField(required=True, max_length=200)

    class Meta:
        model = User
        fields = ["username", "email", "phonenumber", "address", "password1", "password2"]

class OrderForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email')
    phone = forms.CharField(label='Phone', max_length=20)
    items = forms.CharField(label='Items', widget=forms.Textarea)
    address = forms.CharField(max_length=200)
    
    
class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ["name", "price", "description", "photo"]
        

