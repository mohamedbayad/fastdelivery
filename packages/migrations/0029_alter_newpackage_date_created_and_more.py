# Generated by Django 4.1.1 on 2022-12-14 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0028_alter_newpackage_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newpackage',
            name='date_created',
            field=models.CharField(blank=True, default='14-12-2022', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='newpackage',
            name='date_picked_up',
            field=models.CharField(blank=True, default='14-12-2022', max_length=100, null=True),
        ),
    ]
