# Generated by Django 4.1.4 on 2023-02-01 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_alter_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='total_money_net',
            field=models.IntegerField(blank=True, default=0, max_length=100, null=True),
        ),
    ]