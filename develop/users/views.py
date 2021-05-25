
from django.shortcuts import render
from django.views.generic import FormView, CreateView

from . import forms

# Create your views here.
class SignUpView(FormView):
    template_name = 'users/signup.html'
    form_class = forms.SignUpForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)