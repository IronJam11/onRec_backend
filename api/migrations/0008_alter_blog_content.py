# Generated by Django 5.1.4 on 2024-12-22 20:08

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_podcast_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.JSONField(default=list, help_text="Enter JSON data as a list of dictionaries with 'heading' and 'paragraph' keys.", validators=[api.models.validate_json_content]),
        ),
    ]
