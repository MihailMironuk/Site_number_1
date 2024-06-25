# Generated by Django 5.0.6 on 2024-06-06 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Books",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100, verbose_name="Введите название книги"
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        upload_to="books_image/", verbose_name="Загрузите фото"
                    ),
                ),
                ("about_emp", models.TextField(verbose_name="Описание книги")),
                (
                    "author",
                    models.CharField(max_length=100, verbose_name="Автор произведения"),
                ),
                (
                    "books_choices",
                    models.CharField(
                        choices=[
                            ("Триллер", "Триллер"),
                            ("Научная фантастика", "Научная фантастика"),
                            ("История", "История"),
                        ],
                        max_length=100,
                        verbose_name="Выберите жанр книги",
                    ),
                ),
            ],
        ),
    ]
