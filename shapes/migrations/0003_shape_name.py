# Generated by Django 3.2.8 on 2021-10-30 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shapes', '0002_auto_20211031_0010'),
    ]

    operations = [
        migrations.AddField(
            model_name='shape',
            name='name',
            field=models.CharField(default='square', max_length=200),
            preserve_default=False,
        ),
    ]