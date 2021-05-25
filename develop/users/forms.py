from django import forms
from django.forms import widgets
from . import models

class SignUpForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ['username', 'password', 'first_name', 'last_name', 'address']
        widgets = {
            'password': forms.PasswordInput(),
        }
    user_type = forms.ChoiceField(choices=models.User.USER_TYPES)

    def save(self, *args, **kwargs):
        user = super().save(commit=False)
        user.user_type = self.cleaned_data.get("user_type")
        user.save()
    

        