# Generated by Django 4.0.4 on 2022-04-25 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postmodel',
            name='author',
        ),
        migrations.RemoveField(
            model_name='postmodel',
            name='created',
        ),
        migrations.RemoveField(
            model_name='postmodel',
            name='publishDate',
        ),
        migrations.RemoveField(
            model_name='postmodel',
            name='slug',
        ),
    ]
