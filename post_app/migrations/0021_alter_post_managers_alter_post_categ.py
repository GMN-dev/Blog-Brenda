# Generated by Django 4.0.4 on 2022-05-30 19:19

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('post_app', '0020_post_categ'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='post',
            managers=[
                ('postManager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='categ',
            field=models.ManyToManyField(to='post_app.category', verbose_name='Categoria do post:'),
        ),
    ]