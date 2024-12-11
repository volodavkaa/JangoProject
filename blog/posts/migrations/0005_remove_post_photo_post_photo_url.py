# Generated by Django 5.1.3 on 2024-12-11 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_remove_post_photo_url_post_author_post_photo_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='photo',
        ),
        migrations.AddField(
            model_name='post',
            name='photo_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]