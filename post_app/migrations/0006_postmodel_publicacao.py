# Generated by Django 4.0.4 on 2022-05-09 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_app', '0005_alter_postmodel_author_alter_postmodel_datepublish'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='publicacao',
            field=models.DateField(auto_now=True),
        ),
    ]
