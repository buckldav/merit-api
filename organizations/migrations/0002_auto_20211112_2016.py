# Generated by Django 3.1.13 on 2021-11-13 03:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogAPIKey',
            fields=[
                ('organizationapikey_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='organizations.organizationapikey')),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
            options={
                'verbose_name': 'Organization API Key',
                'verbose_name_plural': 'Organization API Keys',
                'ordering': ('-created',),
                'abstract': False,
            },
            bases=('organizations.organizationapikey',),
        ),
        migrations.AlterModelOptions(
            name='organizationapikey',
            options={'ordering': ('-created',), 'verbose_name': 'Organization API Key', 'verbose_name_plural': 'Organization API Keys'},
        ),
    ]
