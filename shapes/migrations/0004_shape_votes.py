# Generated by Django 3.2.8 on 2021-10-30 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shapes', '0003_shape_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='shape',
            name='votes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
