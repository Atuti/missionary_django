# Generated by Django 4.1.3 on 2023-01-23 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rainbow', '0002_rename_testimony_testimony_testimony'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prayer',
            old_name='Prayer',
            new_name='prayer',
        ),
    ]
