# Generated by Django 4.0.3 on 2024-01-23 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fmsApp', '0003_post_department'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-updated']},
        ),
        migrations.AddField(
            model_name='post',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
