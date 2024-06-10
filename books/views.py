from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
import random
from books.models import Books, Poster


def all_books(request):
    if request.method == 'GET':
        books = Books.objects.filter().order_by('-id')
        return render(request, 'all_my_books/all_books.html', {'books': books})


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
