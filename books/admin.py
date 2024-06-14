from django.contrib import admin
from books.models import Books, Poster, ReviewBooks, Tag, AllBooks
from django.utils.safestring import mark_safe

admin.site.register(Books)


class BookPreview(admin.ModelAdmin):
    readonly_fields = ["preview"]

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 200px;">')


admin.site.register(Poster)
admin.site.register(ReviewBooks)
admin.site.register(Tag)
admin.site.register(AllBooks)
