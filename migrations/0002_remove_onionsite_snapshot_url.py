# Generated by Django 5.1.4 on 2025-02-14 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Crawler_frontend", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="onionsite",
            name="snapshot_url",
        ),
    ]
