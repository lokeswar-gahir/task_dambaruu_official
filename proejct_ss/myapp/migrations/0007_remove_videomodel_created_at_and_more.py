# Generated by Django 5.0.4 on 2024-04-19 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_videomodel_created_at_videomodel_modified_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videomodel',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='videomodel',
            name='modified_at',
        ),
    ]
