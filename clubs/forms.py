from django import forms
from django.contrib.auth.models import User
from clubs.models import Club, Deals
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from django.forms.widgets import TextInput
from django.utils.dateparse import parse_duration

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = (
                "username",
                "first_name",
                "last_name",
                "email",
                "password1",
                "password2",
                )

class ClubsForm(ModelForm):
    name = forms.CharField(max_length=30, required=False, help_text='Optional.', label = "Club Name")
    city = forms.CharField(max_length=30, required=False, help_text='Optional.')
    website = forms.CharField(max_length=30, required=False, help_text='Optional.')
    phone = forms.CharField(max_length=30, required=False, help_text='Optional.')

    class Meta:
        model = Club
        
        fields = (
            "name",
            "city",
            "website",
            "phone"

        )

class DealsForm(ModelForm):
    description = forms.CharField(max_length=255, required=False, label = "Description")
    code = forms.CharField(max_length=30, required=True, help_text='Enter a custom code.')

    class Meta:
        model = Deals
        
        fields = (
            "description",
            "code"

        )


