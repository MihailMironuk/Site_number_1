# Generated by Django 5.0.6 on 2024-06-10 08:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_poster_alter_books_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewBooks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('mark', models.IntegerField(default=5)),
                ('books', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_books', to='books.books')),
            ],
        ),
    ]
