# Generated by Django 3.2.6 on 2021-09-24 09:12

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('akapp', '0002_alter_anken_naiyou'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anken',
            name='naiyou',
            field=tinymce.models.HTMLField(max_length=1000, verbose_name='内容'),
        ),
    ]