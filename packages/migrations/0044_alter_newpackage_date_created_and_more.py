# Generated by Django 4.1.4 on 2023-05-11 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0043_alter_newpackage_date_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newpackage',
            name='date_created',
            field=models.CharField(blank=True, default='11-05-2023', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='newpackage',
            name='date_picked_up',
            field=models.CharField(blank=True, default='11-05-2023', max_length=100, null=True),
        ),
    ]