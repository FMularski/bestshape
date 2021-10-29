from django.shortcuts import render
from django.views.generic import TemplateView


class RegisterPageView(TemplateView):
    template_name = 'shapes/register.html'