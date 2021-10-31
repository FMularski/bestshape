from django.urls import path
from .views import GetShapesView, GetVotesRatioView, LoginView, RegisterView, LogoutView, VoteView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('shapes/', GetShapesView.as_view(), name='shapes'),
    path('vote/<pk>/', VoteView.as_view(), name='vote'),
    path('vote-ratio/<pk>/', GetVotesRatioView.as_view(), name='ratio'),
]