# Generated by Django 4.0.6 on 2022-08-02 02:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('first_name', models.CharField(max_length=50, unique=True)),
                ('last_name', models.CharField(max_length=50, unique=True)),
                ('business_name', models.CharField(max_length=50, unique=True)),
                ('phone', models.CharField(max_length=50, unique=True)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]
