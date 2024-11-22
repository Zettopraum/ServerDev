# Generated by Django 5.1.2 on 2024-11-21 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField()),
                ('last_login', models.DateTimeField()),
            ],
        ),
    ]
