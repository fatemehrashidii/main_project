# Generated by Django 3.1.7 on 2021-03-04 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0006_auto_20210304_1452'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_No', models.DecimalField(decimal_places=9, max_digits=610399300)),
                ('score', models.DecimalField(decimal_places=3, max_digits=100, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='sending_response',
            name='score',
        ),
    ]
