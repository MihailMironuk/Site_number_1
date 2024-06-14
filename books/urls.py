from django.urls import path
from . import views

urlpatterns = [

    path('all_books/', views.all_books),

    path('books/', views.books_list_view),
    path('books/<int:id>/', views.books_detail_view),
    path('books/<int:id>/delete/', views.delete_book_view),
    path('books/<int:id>/update/', views.edit_book_view),
    path('create_book/', views.create_book_view),

    path('info/', views.info_view),
    path('hobbies/', views.hobbies_view),
    path('time/', views.current_time_view),
    path('random/', views.random_numbers_view),
]