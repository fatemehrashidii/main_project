# Generated by Django 3.1.7 on 2021-03-05 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0011_auto_20210305_1042'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercises',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=100)),
                ('exercise', models.FileField(upload_to='exercise')),
            ],
        ),
    ]
