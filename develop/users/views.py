from django.forms import widgets
from django.shortcuts import redirect, render, reverse
from django.views.generic import FormView, UpdateView
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from . import mixins
from django import forms as django_forms
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
    success_url = reverse_lazy("core:home")

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
    form_class = forms.EditForm
    template_name = "users/edit.html"
    initial = {"password": "New password"}
    success_message = "Profile Updated"
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        new_password = form.cleaned_data.get("password")
        self.request.user.set_password(new_password)
        return super().form_valid(form)

    def get_object(self, queryset=None):
        return self.request.user
