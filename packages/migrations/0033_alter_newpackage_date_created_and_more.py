# Generated by Django 4.1.4 on 2022-12-25 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0032_alter_newpackage_date_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newpackage',
            name='date_created',
            field=models.CharField(blank=True, default='25-12-2022', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='newpackage',
            name='date_picked_up',
            field=models.CharField(blank=True, default='25-12-2022', max_length=100, null=True),
        ),
    ]
