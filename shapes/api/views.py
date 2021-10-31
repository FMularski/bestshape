from re import I
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from shapes.forms import RegisterForm
from shapes.models import Shape, Vote
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
    permission_classes = [IsAuthenticated]
    def post(self, request):
        logout(request)
        return Response(status.HTTP_200_OK)


class GetShapesView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        shapes = Shape.objects.all()
        serializer = ShapeSerializer(shapes, many=True)
        return Response(serializer.data, status.HTTP_200_OK)


class VoteView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, pk):
        vote = Vote.objects.get(user=request.user)
        shape = Shape.objects.get(pk=pk)

        vote.shape = shape
        vote.save()

        return Response(status.HTTP_200_OK)


class GetVotesRatioView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        shape = Shape.objects.get(pk=pk)
        shape_votes_count = shape.vote_set.all().count()
        all_votes_count = Vote.objects.all().count()

        ratio = shape_votes_count / all_votes_count * 100

        return Response(ratio, status.HTTP_200_OK)

