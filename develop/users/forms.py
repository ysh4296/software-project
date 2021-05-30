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
    
class LoginForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "username"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password"}))   
    
    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        try:
            user = models.User.objects.get(username=username)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("Password is wrong"))
        except models.User.DoesNotExist:
            self.add_error("username", forms.ValidationError("User does not exist"))