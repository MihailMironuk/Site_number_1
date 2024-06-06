from django.db import models


class Books(models.Model):
    BOOKS_CHOICES = (
        ("Роман", "Роман"),
        ("Роман-эпопея", "Роман-эпопея"),
    )
    name = models.CharField(max_length=100, verbose_name='Введите название книги')
    image = models.ImageField(upload_to='books_image/', verbose_name='Загрузите фото')
    about_emp = models.TextField(verbose_name='Описание книги')
    author = models.CharField(max_length=100, verbose_name='Автор произведения')

    def __str__(self):
        return f'{self.name}-{self.books_choices}'

    class Meta:
        verbose_name = 'книгу'
        verbose_name_plural = 'книжки'
