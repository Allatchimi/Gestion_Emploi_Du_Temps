# Generated by Django 4.0.4 on 2022-05-31 01:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('filiére', '0001_initial'),
        ('matiére', '0001_initial'),
        ('enseignant', '0002_rename_code_enseignant_prenom'),
        ('type', '0001_initial'),
        ('salle', '0001_initial'),
        ('groupe', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='cours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('debut', models.DateTimeField(null=True)),
                ('fin', models.DateTimeField(null=True)),
                ('id_Enseignant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='enseignant.enseignant')),
                ('id_Filiere', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='filiére.filiere')),
                ('id_Groupe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='groupe.groupe')),
                ('id_Matiere', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='matiére.matiere')),
                ('id_Salle', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='salle.salle')),
                ('id_Type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='type.type')),
            ],
        ),
    ]
