# Generated by Django 4.1.4 on 2023-05-10 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boxPackages', '0006_alter_newbox_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newbox',
            name='date',
            field=models.CharField(blank=True, default='10-05-2023', max_length=100, null=True),
        ),
    ]