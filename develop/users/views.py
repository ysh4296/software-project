from django.shortcuts import redirect, render, reverse
from django.views.generic import FormView, UpdateView
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from . import mixins

from . import forms, models

# Create your views here.
class SignUpView(mixins.LoggedOutOnlyView, FormView):
    template_name = "users/signup.html"
    form_class = forms.SignUpForm
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def log_out(request):
    logout(request)
    return redirect(reverse("users:login"))


class LoginView(mixins.LoggedOutOnlyView, FormView):

    template_name = "users/login.html"
    form_class = forms.LoginForm
    success_url = reverse_lazy("users:home")

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            if user.user_type == models.User.USER_SELLER:
                self.success_url = reverse_lazy("restaurant:list")
        return super().form_valid(form)


def home(request):
    return render(request, "users/home.html")


class EditView(mixins.LoggedInOnlyView, SuccessMessageMixin, UpdateView):
    model = models.User
    template_name = "users/edit.html"
    fields = (
        "password",
        "first_name",
        "last_name",
        "address",
    )
    initial = {"password": "New password"}
    success_message = "Profile Updated"
    success_url = reverse_lazy("users:home")

    def get_object(self, queryset=None):
        return self.request.user

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields["password"].widget.attrs = {
            "placeholder": "Password",
            "class": "form-control",
        }
        form.fields["first_name"].widget.attrs = {
            "placeholder": "First Name",
            "class": "form-control",
        }
        form.fields["last_name"].widget.attrs = {
            "placeholder": "Last Name",
            "class": "form-control",
        }
        form.fields["address"].widget.attrs = {
            "placeholder": "Address",
            "class": "form-control",
        }
        return form

    def form_valid(self, form):
        new_password = form.cleaned_data.get("password")
        self.request.user.set_password(new_password)
        return super().form_valid(form)
