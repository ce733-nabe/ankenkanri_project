# Generated by Django 3.2.6 on 2021-09-29 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akapp', '0002_alter_shuho_anken'),
    ]

    operations = [
        migrations.AddField(
            model_name='anken',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]