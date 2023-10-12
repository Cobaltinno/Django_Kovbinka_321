# Generated by Django 4.2.5 on 2023-10-12 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категорія для публікації', 'verbose_name_plural': 'Категорії для публікацій'},
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='', verbose_name='Слаг'),
        ),
        migrations.AlterField(
            model_name='article',
            name='main_page',
            field=models.BooleanField(default=False, help_text='Показуватина головній сторінці', verbose_name='Головна'),
        ),
    ]
