# Generated by Django 4.1.1 on 2022-12-13 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0027_remove_exchangerequest_package_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newpackage',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newpackage',
            name='article_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='newpackage',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='newpackage',
            name='client_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='newpackage',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='newpackage',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='newpackage',
            name='remark',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
    ]