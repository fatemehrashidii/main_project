# Generated by Django 3.1.7 on 2021-03-05 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0010_videos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='videos',
            old_name='vids',
            new_name='video',
        ),
    ]
