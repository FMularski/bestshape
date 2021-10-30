from django.shortcuts import redirect, reverse


class RedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        if request.user.is_authenticated and request.path in ['/login/', '/register/']:
            return redirect(reverse('index_page', ))

        response = self.get_response(request)

        return response
