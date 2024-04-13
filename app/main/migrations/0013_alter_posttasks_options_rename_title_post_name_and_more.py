# Generated by Django 4.2.5 on 2024-03-31 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_categories_is_favorite_post_is_favorite'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='posttasks',
            options={'ordering': ['name'], 'verbose_name': 'Задача', 'verbose_name_plural': 'Задачі'},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='posttasks',
            old_name='title',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='POST_URL'),
        ),
    ]