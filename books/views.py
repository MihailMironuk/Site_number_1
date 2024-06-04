from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import random


def info_view(request):
    if request.method == "GET":
        return HttpResponse('Привет, меня зовут Селедцов Михаил, мне 23')


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


