# Generated by Django 3.1.13 on 2021-11-13 03:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0002_auto_20211112_2016'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogapikey',
            options={'ordering': ('-created',), 'verbose_name': 'Blog API Key', 'verbose_name_plural': 'Blog API Keys'},
        ),
    ]
