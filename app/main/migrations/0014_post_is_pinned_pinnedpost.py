# Generated by Django 4.2.5 on 2024-04-01 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_posttasks_options_rename_title_post_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_pinned',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='PinnedPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.categories')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.post')),
            ],
        ),
    ]