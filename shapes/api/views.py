from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from shapes.forms import RegisterForm
from .serializers import UserSerializer
import json


class RegisterView(APIView):
    def post(self, request):
        form = RegisterForm(data=request.data)
        if form.is_valid():
            user = form.save()
            serializer = UserSerializer(user)
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            return Response(form.errors, status.HTTP_400_BAD_REQUEST)



