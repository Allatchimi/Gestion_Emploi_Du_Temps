# Generated by Django 4.0.4 on 2022-06-02 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classe',
            name='code',
            field=models.CharField(max_length=2, null=True),
        ),
    ]
