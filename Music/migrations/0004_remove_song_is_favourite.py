# Generated by Django 2.2.3 on 2019-09-15 02:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0003_song_is_favourite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='is_favourite',
        ),
    ]
