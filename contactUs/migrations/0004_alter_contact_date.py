# Generated by Django 4.1.4 on 2023-01-10 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactUs', '0003_contact_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.CharField(blank=True, default='10-01-2023', max_length=100, null=True),
        ),
    ]