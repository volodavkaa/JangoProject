# Generated by Django 5.1.3 on 2024-12-16 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_remove_post_photo_post_photo_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='post_photos/'),
        ),
    ]