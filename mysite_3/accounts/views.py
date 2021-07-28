from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView


class UserRegisterView(CreateView):
    model = User
    template_name = "register.html"
    success_url = reverse_lazy("polls:index")
    form_class = UserCreationForm