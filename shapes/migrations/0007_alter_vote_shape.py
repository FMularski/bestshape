# Generated by Django 3.2.8 on 2021-10-31 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shapes', '0006_remove_user_shape'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='shape',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='shapes.shape'),
        ),
    ]
