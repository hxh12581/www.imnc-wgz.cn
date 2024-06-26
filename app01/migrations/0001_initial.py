# Generated by Django 3.2.9 on 2023-10-27 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=25)),
                ('username', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=25)),
                ('group_id', models.CharField(max_length=25)),
                ('count', models.IntegerField(default=0)),
                ('userFace', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=25)),
            ],
        ),
    ]
