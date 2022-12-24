# Generated by Django 4.1.1 on 2022-10-13 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0011_alter_newpackage_date_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newpackage',
            name='date_created',
            field=models.CharField(blank=True, default='13-10-2022 21:23', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='newpackage',
            name='date_picked_up',
            field=models.CharField(blank=True, default='13-10-2022 21:23', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='newpackage',
            name='etat',
            field=models.CharField(blank=True, choices=[('EN ATTENTE DE RAMASSAGE', 'EN ATTENTE DE RAMASSAGE'), ('Echange', 'Echange'), ('Ramassée', 'Ramassée'), ('Annulée', 'Annulée'), ('Livrée', 'Livrée'), ('Refusée', 'Refusée'), ('Pas de réponse', 'Pas de réponse'), ('Retournée/Annulée', 'Retournée/Annulée'), ('Retoure/Echange', 'Retoure/Echange'), ('Retournée/Refusée', 'Retournée/Refusée')], default='EN ATTENTE DE RAMASSAGE', max_length=100, null=True),
        ),
    ]
