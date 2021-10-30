from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import RegisterForm


class RegisterPageView(TemplateView):
    template_name = 'shapes/register.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = RegisterForm
        return context


class LoginPageView(TemplateView):
    template_name = 'shapes/login.html'