# Generated by Django 2.2.3 on 2019-09-18 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0005_album_is_favourite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_logo',
            field=models.FileField(upload_to=''),
        ),
    ]