# Generated by Django 3.1.3 on 2023-02-15 13:38

import connection.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connection', '0003_auto_20230214_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='path',
            field=models.FileField(default='data/', upload_to=connection.models.pathToData),
        ),
    ]