from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_delete, post_save


class User(AbstractUser):
    pass


class Shape(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='shapes')


class Vote(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shape = models.ForeignKey(Shape, on_delete=models.CASCADE, null=True)


@receiver(post_delete, sender=Shape)
def delete_shape_img_file(instance, *args, **kwargs):
    instance.image.delete()


@receiver(post_save, sender=User)
def create_vote_for_user(instance, created, *args, **kwargs):
    if created:
        Vote.objects.create(user=instance)
