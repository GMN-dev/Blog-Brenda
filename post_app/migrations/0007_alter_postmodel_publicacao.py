# Generated by Django 4.0.4 on 2022-05-09 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_app', '0006_postmodel_publicacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='publicacao',
            field=models.CharField(max_length=250),
        ),
    ]
