# Generated by Django 2.2.3 on 2019-07-24 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0002_auto_20190724_2012'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='is_favourite',
            field=models.BooleanField(default=False),
        ),
    ]
