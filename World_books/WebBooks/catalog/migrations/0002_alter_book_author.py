# Generated by Django 4.1.3 on 2023-02-22 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(help_text='Выберите атвора книги', to='catalog.author', verbose_name='Язык книги'),
        ),
    ]
