# Generated by Django 4.1.4 on 2023-05-11 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactUs', '0009_alter_contact_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.CharField(blank=True, default='11-05-2023', max_length=100, null=True),
        ),
    ]
