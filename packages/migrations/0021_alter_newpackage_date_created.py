# Generated by Django 4.1.1 on 2022-10-28 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0020_alter_newpackage_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newpackage',
            name='date_created',
            field=models.CharField(blank=True, default='28-10-2022', max_length=100, null=True),
        ),
    ]