# Generated by Django 5.0.7 on 2024-07-11 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0005_rename_playlist_name_playlist_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Codes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=15)),
            ],
        ),
    ]
