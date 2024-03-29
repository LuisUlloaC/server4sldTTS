# Generated by Django 3.1.3 on 2023-02-14 14:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connection', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='audio',
            name='language',
            field=models.TextField(default='es', max_length=50),
        ),
        migrations.AlterField(
            model_name='audio',
            name='file_name',
            field=models.TextField(default=datetime.datetime(2023, 2, 14, 9, 3, 34, 552715), max_length=1000),
        ),
        migrations.AlterField(
            model_name='audio',
            name='text',
            field=models.TextField(default='this is a test text', max_length=2000),
        ),
    ]
