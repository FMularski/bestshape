from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.RegisterPageView.as_view(), name='register_page'),
    path('login/', views.LoginPageView.as_view(), name='login_page'),
    path('', views.IndexPageView.as_view(), name='index_page')
]