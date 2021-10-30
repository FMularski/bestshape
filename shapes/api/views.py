from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from shapes.forms import RegisterForm
from shapes.models import Shape
from .serializers import UserSerializer, ShapeSerializer


class RegisterView(APIView):
    def post(self, request):
        form = RegisterForm(data=request.data)
        if form.is_valid():
            user = form.save()
            serializer = UserSerializer(user)
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            return Response(form.errors, status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return Response(status.HTTP_200_OK)
        
        return Response('Invalid credentials', status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response(status.HTTP_200_OK)


class GetShapesView(APIView):
    def get(self, request):
        shapes = Shape.objects.all()
        serializer = ShapeSerializer(shapes, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

