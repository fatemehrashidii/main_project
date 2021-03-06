# Generated by Django 3.1.7 on 2021-03-06 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0012_exercises'),
    ]

    operations = [
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_number', models.DecimalField(decimal_places=0, max_digits=610399300)),
                ('date', models.DateTimeField(auto_now=True)),
                ('score', models.DecimalField(decimal_places=2, max_digits=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student_Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_address', models.EmailField(max_length=50)),
                ('student_number', models.IntegerField(default=False)),
                ('password', models.IntegerField(default=False, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher_Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_address', models.EmailField(max_length=50)),
                ('password', models.IntegerField(default=False, max_length=20)),
            ],
        ),
        migrations.RenameField(
            model_name='sending_response',
            old_name='student_No',
            new_name='student_number',
        ),
    ]
