# Generated by Django 4.1.1 on 2022-11-01 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='/media/default/default_profile.webp', null=True, upload_to='profiles/%Y/%m/%d'),
        ),
    ]
