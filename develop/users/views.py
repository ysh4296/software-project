
from django.shortcuts import redirect, render, reverse
from django.views.generic import FormView, CreateView, UpdateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserChangeForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from . import forms, models

# Create your views here.
class SignUpView(FormView):
    template_name = 'users/signup.html'
    form_class = forms.SignUpForm
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class LoginView(FormView):

    template_name = "users/login.html"
    form_class = forms.LoginForm
    success_url = reverse_lazy("users:home")

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)

def home(request):
    return render(request, 'users/home.html')

class EditView(SuccessMessageMixin, UpdateView):
    model = models.User
    template_name = "users/edit.html"
    fields = (
        "password",
        "first_name",
        "last_name",
        "address",
    )
    success_message = "Profile Updated"
    success_url = reverse_lazy("users:home")

    def get_object(self, queryset=None):
        return self.request.user

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields["password"].widget.attrs = {"placeholder": "Password"}
        form.fields["first_name"].widget.attrs = {"placeholder": "First Name"}
        form.fields["last_name"].widget.attrs = {"placeholder": "Last Name"}
        form.fields["address"].widget.attrs = {"placeholder": "Address"}
        return form