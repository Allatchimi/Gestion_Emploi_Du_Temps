# Generated by Django 4.0.4 on 2022-06-03 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cours', '0004_rename_id_enseignant_cours_enseignant_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cours',
            name='debut',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='cours',
            name='fin',
            field=models.TimeField(null=True),
        ),
    ]
