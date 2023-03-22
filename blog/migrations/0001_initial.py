# Generated by Django 4.1.3 on 2023-01-26 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=350)),
                ('slug', models.SlugField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('news', models.TextField()),
                ('intro', models.TextField()),
                ('image', models.ImageField(upload_to='news_images')),
            ],
            options={
                'verbose_name_plural': 'News',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=350)),
                ('date', models.DateField(auto_now_add=True)),
                ('slug', models.SlugField()),
                ('blog', models.TextField()),
                ('intro', models.TextField()),
                ('image', models.ImageField(upload_to='image_uploads')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('comment', models.TextField()),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.news')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.post')),
            ],
        ),
    ]
