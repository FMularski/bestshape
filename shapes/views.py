from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RegisterForm


class RegisterPageView(TemplateView):
    template_name = 'shapes/register.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = RegisterForm
        return context


class LoginPageView(TemplateView):
    template_name = 'shapes/login.html'


class IndexPageView(LoginRequiredMixin, TemplateView):
    template_name = 'shapes/index.html'
    login_url = '/login/'