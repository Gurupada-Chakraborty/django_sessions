# Generated by Django 2.2.3 on 2019-09-16 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0004_remove_song_is_favourite'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='is_favourite',
            field=models.BooleanField(default=False),
        ),
    ]
