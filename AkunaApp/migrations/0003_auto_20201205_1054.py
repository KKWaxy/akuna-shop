# Generated by Django 3.1.1 on 2020-12-05 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AkunaApp', '0002_auto_20201205_1040'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorie',
            name='description',
            field=models.TextField(blank=True, max_length='500', null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='categorie',
            name='libelle',
            field=models.CharField(max_length=150, verbose_name='Libelle'),
        ),
    ]
