from django.urls import path
from . import views

urlpatterns = [
    path("all_books/", views.AllBooksView.as_view(), name="all_books"),
    path("books/", views.BooksListView.as_view(), name="books_list"),
    path("books/<int:id>/", views.BooksDetailView.as_view(), name="books-detail"),
    path(
        "books/<int:id>/delete/", views.BooksDeleteView.as_view(), name="books-delete"
    ),
    path("books/<int:id>/update/", views.EditBookView.as_view(), name="edit_book"),
    path("create_book/", views.CreateBookView.as_view(), name="create_book"),
    path("search/", views.SearchView.as_view(), name="search"),
]
