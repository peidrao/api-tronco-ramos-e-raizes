# Generated by Django 3.2.3 on 2021-05-23 23:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('midia', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='audio',
            old_name='file',
            new_name='audio_album',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='image',
            new_name='images',
        ),
        migrations.RenameField(
            model_name='video',
            old_name='link_video',
            new_name='video_album',
        ),
        migrations.RenameField(
            model_name='video',
            old_name='video',
            new_name='videos',
        ),
    ]
