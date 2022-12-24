# Generated by Django 4.1.1 on 2022-12-18 18:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('adminManager', '0006_remove_profilemandelivery_set_packages_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='addpackage',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='addpackage',
            name='man_delivery',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adminManager.profilemandelivery'),
        ),
    ]
