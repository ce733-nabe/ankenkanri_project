# Generated by Django 3.2.6 on 2021-09-28 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('akapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shuho',
            name='anken',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='akapp.anken', verbose_name='案件'),
        ),
    ]