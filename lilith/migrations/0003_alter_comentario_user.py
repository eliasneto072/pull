# Generated by Django 4.2.1 on 2023-05-10 20:55

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lilith', '0002_alter_comentario_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='user',
            field=models.ForeignKey(default=django.contrib.auth.models.AbstractUser, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
