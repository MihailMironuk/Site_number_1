from django.urls import path
from . import views

urlpatterns = [

    path('all_books/', views.all_books),

    path('books', views.BooksListView.as_view()),
    path('books/<int:id>/', views.BooksDetailView.as_view()),
    path('books/<int:id>/delete/', views.BooksDeleteView.as_view()),
    path('books/<int:id>/update/', views.EditBookView.as_view()),
    path('create_book/', views.CreateBookView.as_view()),
    path('search/', views.SearchView.as_view(), name='search'),

    # path('info/', views.info_view),
    # path('hobbies/', views.hobbies_view),
    # path('time/', views.current_time_view),
    # path('random/', views.random_numbers_view),
]
