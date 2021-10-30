from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_delete


class Shape(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='shapes')
    votes = models.PositiveIntegerField(default=0)


class User(AbstractUser):
    shape = models.ForeignKey(Shape, on_delete=models.SET_NULL, null=True)


@receiver(post_delete, sender=Shape)
def delete_shape_handler(instance, *args, **kwargs):
    instance.image.delete()

