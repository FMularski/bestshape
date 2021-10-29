from django.shortcuts import render
from django.views.generic import View


class RegisterView(View):
    def get(self, request):
        context = {}
        return render(request, 'shapes/register.html', context)