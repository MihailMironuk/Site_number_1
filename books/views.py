from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from books.models import Books, Poster
from django.views import generic
from . import forms, models


class AllBooksView(generic.ListView):
    template_name = "all_books/all_books.html"
    context_object_name = "books"

    def get_queryset(self):
        return models.AllBooks.objects.filter().order_by("-id")


# Кнопка поиска


class SearchView(generic.ListView):
    template_name = "books/books_list.html"
    context_object_name = "books"
    paginate_by = 5

    def get_queryset(self):
        return Books.objects.filter(name__icontains=self.request.GET.get("q")).order_by(
            "-id"
        )

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.request.GET.get("q")
        return context


class EditBookView(generic.UpdateView):
    template_name = "books/edit_book.html"
    form_class = forms.BookForm
    success_url = "/books/"

    def get_object(self, **kwargs):
        book_id = self.kwargs.get("id")
        return get_object_or_404(Books, id=book_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(EditBookView, self).form_valid(form=form)


class BooksDeleteView(generic.DeleteView):
    template_name = "books/confirm_book_delete.html"
    success_url = "/books/"

    def get_object(self, **kwargs):
        book_id = self.kwargs.get("id")
        return get_object_or_404(Books, id=book_id)


class CreateBookView(generic.CreateView):
    template_name = "books/create_book.html"
    form_class = forms.BookForm
    success_url = "/books/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateBookView, self).form_valid(form=form)


class BooksListView(generic.ListView):
    template_name = "books/books_list.html"
    context_object_name = "books"
    model = Books
    ordering = ["-id"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posters"] = Poster.objects.order_by("-id")
        return context


class BooksDetailView(generic.DetailView):
    template_name = "books/books_detail.html"
    context_object_name = "book"

    def get_object(self, **kwargs):
        book_id = self.kwargs.get("id")
        return get_object_or_404(Books, id=book_id)


# CRUD CREATE READ UPDATE DELETE

# def all_books(request):
#     if request.method == 'GET':
#         books = Books.objects.filter().order_by('-id')
#         return render(request, 'all_books/all_books.html', {'books': books})

# def edit_book_view(request, id):
#     book_id = get_object_or_404(Books, id=id)
#     if request.method == 'POST':
#         form = forms.BookForm(request.POST, instance=book_id)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('<h3> Book updated!</h3>'
#                                 '<a href="/books/">На список книг</a>')
#     else:
#         form = forms.BookForm(instance=book_id)
#     return render(request,
#                   'books/edit_book.html',
#                   {'form': form,
#                    'book_id': book_id
#                    })

# def delete_book_view(request, id):
#     book_id = get_object_or_404(Books, id=id)
#     book_id.delete()
#     return HttpResponse('<h3> Book deleted</h3>'
#                         '<a href="/books/">На список книг</a>')

# def create_book_view(request):
#     if request.method == 'POST':
#         form = forms.BookForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('<h3> Book Created!</h3>'
#                                 '<a href="/books/">На список книг</a>')
#     else:
#         form = forms.BookForm()
#
#         return render(request,
#                       'books/create_book.html',
#                       {'form': form})

# def books_list_view(request):
#     if request.method == 'GET':
#         query = Books.objects.filter().order_by('-id')
#         posters = Poster.objects.filter().order_by('-id')
#         return render(
#             request,
#             'books/books_list.html',
#             context={
#                 'books': query,
#                 'posters': posters,
#             }
#
#         )


# def books_detail_view(request, id):
#     if request.method == 'GET':
#         book_id = get_object_or_404(Books, id=id)
#         return render(
#             request,
#             'books/books_detail.html',
#             context={
#                 'emp_id': book_id
#             }
#
#         )
