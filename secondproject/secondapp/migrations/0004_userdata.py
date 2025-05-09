# Generated by Django 5.0.1 on 2025-01-02 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondapp', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('email', models.EmailField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=128)),
            ],
            options={
                'db_table': 'userdata',
            },
        ),
    ]
