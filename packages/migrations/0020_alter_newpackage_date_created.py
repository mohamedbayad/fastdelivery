# Generated by Django 4.1.1 on 2022-10-28 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0019_alter_newpackage_date_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newpackage',
            name='date_created',
            field=models.CharField(blank=True, default='28-10-22', max_length=100, null=True),
        ),
    ]