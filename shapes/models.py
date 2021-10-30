from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Shape(models.Model):
    image = models.ImageField(upload_to='shapes')