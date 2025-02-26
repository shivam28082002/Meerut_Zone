import re
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import *


class UserForm(forms.ModelForm):
    """
    Create ModelForm based on User Model.
    """
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        """
        Class meta used for User
        """
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']

    def __init__(self, *args, **kwargs):
        email = kwargs.pop('email', None) 
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].label = 'First Name'
        self.fields['last_name'].label = 'Last Name'
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True
        self.fields['password'].required = True
        self.fields['password'].label = 'Password'
        self.fields['password'].widget = forms.widgets.PasswordInput(attrs={'type': 'password'})
        self.fields['first_name'].widget.attrs['placeholder'] = 'First name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Email address'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'


        if email:
            self.fields['email'].initial = email 
            self.fields['email'].widget.attrs['disabled'] = True

    def clean(self):
        cleaned_data = super().clean()
        for field in cleaned_data:
            if isinstance(cleaned_data[field], str):
                cleaned_data[field] = cleaned_data[field].strip()
                cleaned_data[field] = ' '.join(cleaned_data[field].split())
        return cleaned_data
    

class UserProfileForm(forms.ModelForm):
    """
      Create ModelForm based on User Model.
    """
    gender = forms.ChoiceField(choices=[('','Select Gender'),('Male','Male'),('Female','Female'),('Other','Other')])

    class Meta:
        """
        Class meta used for User
        """
        model = UserProfile
        fields = ['phone', 'gender', 'date_of_birth']
    def __init__(self, user=None, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['phone'].label = 'Phone Number'
        self.fields['phone'].required = True
        self.fields['phone'].widget.attrs['placeholder'] = '+91 0000000000'
        self.fields['gender'].required = True
        self.fields['date_of_birth'].required = True
        self.fields['gender'].label = 'Select Gender'
        self.fields['date_of_birth'].widget.attrs['placeholder'] = 'MM/DD/YYYY'
        self.fields['date_of_birth'].widget = forms.widgets.DateInput(attrs={'type': 'date'})
        self.fields['date_of_birth'].label = 'Date of Birth'


class LoginForm(forms.Form):
    """
         Create LoginForm with specific form fields.
    """
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder'] = "Enter Email"
        self.fields['password'].widget.attrs['placeholder'] = "Enter your Password"



class PasswordChangeForm(forms.Form):
    """
    A form that change the password of the login user.
    """

    error_messages = {
        "password_mismatch": _("The confirm password and password fields didn’t match."),
    }

    old_password = forms.CharField(
        label=_("Old password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),

    )

    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )
    password2 = forms.CharField(
        label=_("Confirm Password"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
    )

    def __init__(self, user=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.req_user = user