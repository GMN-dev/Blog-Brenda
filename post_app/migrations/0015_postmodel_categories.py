# Generated by Django 4.0.4 on 2022-05-16 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_app', '0014_categorymodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='categories',
            field=models.ManyToManyField(to='post_app.categorymodel'),
        ),
    ]
