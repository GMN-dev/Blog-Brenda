# Generated by Django 4.0.4 on 2022-05-13 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post_app', '0010_postmodel_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postmodel',
            name='categories',
        ),
        migrations.DeleteModel(
            name='Criar_Categoria',
        ),
    ]
