# Generated by Django 5.0.7 on 2024-07-23 12:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0003_rename_clip_playlistclips_clip_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matchclip',
            name='match',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='match', to='youtube.matchdetail'),
        ),
        migrations.AlterField(
            model_name='playlistclips',
            name='clip_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clips', to='youtube.matchclip'),
        ),
        migrations.AlterField(
            model_name='playlistclips',
            name='playlist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='playlists', to='youtube.playlist'),
        ),
    ]
