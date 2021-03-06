# Generated by Django 3.2.8 on 2021-10-31 16:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shapes', '0004_shape_votes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shape',
            name='votes',
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shape', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shapes.shape')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
