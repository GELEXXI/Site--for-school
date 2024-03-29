# Generated by Django 4.2.5 on 2024-03-27 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_posttasks_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('img', models.ImageField(blank=True, upload_to='post', verbose_name='Фото поста')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='URL')),
                ('is_visible', models.BooleanField(default=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.categories')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Пости',
                'ordering': ['id'],
            },
        ),
    ]
