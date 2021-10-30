# Generated by Django 3.2.8 on 2021-10-30 22:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shapes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shape',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='shapes')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='shape',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shapes.shape'),
        ),
    ]
