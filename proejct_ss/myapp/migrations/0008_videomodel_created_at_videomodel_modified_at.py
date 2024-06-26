# Generated by Django 5.0.4 on 2024-04-19 17:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_remove_videomodel_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='videomodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='videomodel',
            name='modified_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
