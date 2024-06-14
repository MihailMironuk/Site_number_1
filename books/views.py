from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
import random
from books.models import Books, Poster
from django.views import generic
from . import forms


class SearchView(generic.ListView):
    template_name = "books/books_list.html"
    context_object_name = "books"
    paginate_by = 5

    def get_queryset(self):
        return Books.objects.filter(name__icontains=self.request.GET.get('q')).order_by('-id')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context




# CRUD CREATE READ UPDATE DELETE


# Редактирование

class EditBookView(generic.UpdateView):
    template_name = 'books/edit_book.html'
    form_class = forms.BookForm
    success_url = '/books/'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(Books, id=book_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(EditBookView, self).form_valid(form=form)


def edit_book_view(request, id):
    book_id = get_object_or_404(Books, id=id)
    if request.method == 'POST':
        form = forms.BookForm(request.POST, instance=book_id)
        if form.is_valid():
            form.save()
            return HttpResponse('<h3> Book updated!</h3>'
                                '<a href="/books/">На список книг</a>')
    else:
        form = forms.BookForm(instance=book_id)
    return render(request,
                  'books/edit_book.html',
                  {'form': form,
                   'book_id': book_id
                   })


# Удаление
class BooksDeleteView(generic.DeleteView):
    template_name = 'books/confirm_book_delete.html'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(Books, id=book_id)


def delete_book_view(request, id):
    book_id = get_object_or_404(Books, id=id)
    book_id.delete()
    return HttpResponse('<h3> Book deleted</h3>'
                        '<a href="/books/">На список книг</a>')


# Создание
class CreateBookView(generic.CreateView):
    template_name = 'books/create_book.html'
    form_class = forms.BookForm
    success_url = '/create_book/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateBookView, self).form_valid(form=form)


def create_book_view(request):
    if request.method == 'POST':
        form = forms.BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('<h3> Book Created!</h3>'
                                '<a href="/books/">На список книг</a>')
    else:
        form = forms.BookForm()

        return render(request,
                      'books/create_book.html',
                      {'form': form})


def all_books(request):
    if request.method == 'GET':
        books = Books.objects.filter().order_by('-id')
        return render(request, 'all_books/all_books.html', {'books': books})


class BooksListView(generic.ListView):
    template_name = "books/books_list.html"
    context_object_name = 'books'
    model = Books
    ordering = ['-id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posters'] = Poster.objects.order_by('-id')
        return context


def books_list_view(request):
    if request.method == 'GET':
        query = Books.objects.filter().order_by('-id')
        posters = Poster.objects.filter().order_by('-id')
        return render(
            request,
            'books/books_list.html',
            context={
                'books': query,
                'posters': posters,
            }

        )


class BooksDetailView(generic.DetailView):
    template_name = 'books/books_detail.html'
    context_object_name = 'book_id'

    def get_object(self, **kwargs):
        book_id = get_object_or_404('id')
        return get_object_or_404(Books, id=book_id)


def books_detail_view(request, id):
    if request.method == 'GET':
        book_id = get_object_or_404(Books, id=id)
        return render(
            request,
            'books/books_detail.html',
            context={
                'emp_id': book_id
            }

        )


def info_view(request):
    if request.method == "GET":
        return HttpResponse('Привет, меня зовут Селедцов Михаил, мне 23 года')


def hobbies_view(request):
    if request.method == "GET":
        return HttpResponse('Я играю в компик')


def current_time_view(request):
    if request.method == "GET":
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return HttpResponse(f"Текущее время: {now}")


def random_numbers_view(request):
    if request.method == "GET":
        random_number = random.randint(1, 150)
        return HttpResponse(f"Случайные числа: {random_number}")
