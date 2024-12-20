# Generated by Django 5.1.2 on 2024-11-21 12:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('genres', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('release_date', models.DateField()),
                ('rating', models.IntegerField()),
                ('genre_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='genres.genres', verbose_name='contents')),
            ],
        ),
    ]
