# Generated by Django 3.1.1 on 2020-12-21 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AkunaApp', '0005_auto_20201205_1133'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetailCommande',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pu_prod', models.IntegerField(help_text='Prix Unitaire du produit.', verbose_name='PU')),
                ('quantite', models.IntegerField(default=1, verbose_name='Quantité')),
                ('create_date', models.DateTimeField(auto_now_add=True, help_text='Date de création', verbose_name='Date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Date de modification')),
                ('commande', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AkunaApp.commande')),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AkunaApp.produit')),
            ],
            options={
                'verbose_name': 'liste',
                'verbose_name_plural': 'listes',
            },
        ),
        migrations.CreateModel(
            name='PanierElementModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.IntegerField(default=1, verbose_name='Quantite')),
                ('date_ajout', models.DateTimeField(auto_now_add=True, verbose_name="Date d'ajout")),
                ('date_modif', models.DateTimeField(auto_now=True, verbose_name='Date modification')),
            ],
            options={
                'verbose_name': 'PanierElementModel',
                'verbose_name_plural': 'PanierElementModels',
                'db_table': '',
                'ordering': ['date_ajout'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PanierModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Date de création')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Date de modification')),
            ],
            options={
                'verbose_name': 'PanierModel',
                'verbose_name_plural': 'PanierModels',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(upload_to='clients_avatar', verbose_name='Photo de profile')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Date de création')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Date de modification')),
                ('client', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='AkunaApp.client')),
            ],
            options={
                'verbose_name': 'client_profile',
                'verbose_name_plural': 'client_profiles',
                'managed': True,
            },
        ),
        migrations.DeleteModel(
            name='Liste',
        ),
        migrations.AddField(
            model_name='panierelementmodel',
            name='panier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AkunaApp.paniermodel'),
        ),
        migrations.AddField(
            model_name='panierelementmodel',
            name='produit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='AkunaApp.produit'),
        ),
    ]
