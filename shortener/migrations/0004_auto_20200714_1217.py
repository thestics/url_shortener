# Generated by Django 3.0.8 on 2020-07-14 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0003_urls_used_times'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Urls',
            new_name='Url',
        ),
    ]
