# Generated by Django 4.1.1 on 2022-10-10 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0009_alter_newpackage_amount_withdrawn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newpackage',
            name='date_created',
            field=models.CharField(blank=True, default='10-10-2022 20:13', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='newpackage',
            name='date_picked_up',
            field=models.CharField(blank=True, default='10-10-2022 20:13', max_length=100, null=True),
        ),
    ]