# Generated by Django 3.1.13 on 2022-05-16 17:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20211213_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='date_created',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2021, 12, 15, 0, 0)),
            preserve_default=False,
        ),
    ]