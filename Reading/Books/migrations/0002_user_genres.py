# Generated by Django 4.0.1 on 2022-06-24 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='genres',
            field=models.JSONField(default=0),
            preserve_default=False,
        ),
    ]
