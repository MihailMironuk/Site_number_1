from django.db import models


class Poster(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="sliders/")

    def __str__(self):
        return self.name


class Books(models.Model):
    GENRE = (
        ("Роман", "Роман"),
        ("Роман-эпопея", "Роман-эпопея"),
    )
    name = models.CharField(max_length=100, verbose_name="Введите название книги")
    image = models.ImageField(upload_to="books_image/", verbose_name="Загрузите фото")
    about_emp = models.TextField(verbose_name="Описание книги")
    genre = models.CharField(
        max_length=20, choices=GENRE, verbose_name="Укажите жанр книги", null=True
    )
    author = models.CharField(max_length=100, verbose_name="Автор произведения")

    def __str__(self):
        return f"{self.name}-{self.GENRE}"

    class Meta:
        verbose_name = "книгу"
        verbose_name_plural = "книжки"


class ReviewBooks(models.Model):
    books = models.ForeignKey(
        Books, on_delete=models.CASCADE, related_name="review_books"
    )
    text = models.TextField()
    mark = models.IntegerField(default=5)

    def __str__(self):
        return f"{self.books} - {self.mark}"


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class AllBooks(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField(default=100)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.title} - {self.price}"
