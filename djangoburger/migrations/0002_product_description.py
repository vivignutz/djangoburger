# Generated by Django 4.1.4 on 2022-12-28 21:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoburger', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(),
            preserve_default=False,
        ),
    ]
