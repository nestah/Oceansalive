# Generated by Django 4.0.3 on 2024-02-08 12:09

from django.db import migrations, models
import fmsApp.models


class Migration(migrations.Migration):

    dependencies = [
        ('fmsApp', '0004_alter_post_options_post_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='file_path',
            field=models.FileField(blank=True, null=True, upload_to=fmsApp.models.post_file_path),
        ),
    ]
