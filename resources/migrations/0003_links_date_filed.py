# Generated by Django 4.1.3 on 2023-03-21 07:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0002_links'),
    ]

    operations = [
        migrations.AddField(
            model_name='links',
            name='date_filed',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]