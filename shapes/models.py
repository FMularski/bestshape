from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_delete


class Shape(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='shapes')


class User(AbstractUser):
    shape = models.ForeignKey(Shape, on_delete=models.SET_NULL, null=True)


class Vote(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shape = models.ForeignKey(Shape, on_delete=models.CASCADE)


@receiver(post_delete, sender=Shape)
def delete_shape_handler(instance, *args, **kwargs):
    instance.image.delete()

