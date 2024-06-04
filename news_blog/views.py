from django.shortcuts import render
from django.http import HttpResponse


def news_blog_view(request):
    if request.method == 'GET':
        return HttpResponse('Здесь очень интересные новости')


def hello_view(request):
    if request.method == 'GET':
        return HttpResponse('Привет')
