from django import forms
from . import models

class SignUpForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ['username', 'password', 'first_name', 'last_name','user_type', 'address']

        