from django.contrib import admin
from books.models import Books, Poster, ReviewBooks, Tag, AllBooks

admin.site.register(Books)
admin.site.register(Poster)
admin.site.register(ReviewBooks)
admin.site.register(Tag)
admin.site.register(AllBooks)

