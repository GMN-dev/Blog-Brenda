# Generated by Django 4.0.4 on 2022-05-16 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_app', '0011_remove_postmodel_categories_delete_criar_categoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='categoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inputCategory', models.CharField(max_length=250, verbose_name='Adicionar Categoria')),
            ],
        ),
    ]