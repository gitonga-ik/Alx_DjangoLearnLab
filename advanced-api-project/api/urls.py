from django.urls import path
from .views import BookCreateView,BookDetailView,BookListView,BookUpdateView,BookDeleteView
from rest_framework.authtoken import views

urlpatterns = [
    path("get-token", views.obtain_auth_token, name="auth-token"),
    path("books/", BookListView.as_view(), name="list-books"),
    path("books/create", BookCreateView.as_view(), name="add-book"),
    path("books/<int:pk>", BookDetailView.as_view(), name="book-details"),
    path("books/update/<int:pk>", BookUpdateView.as_view(), name="update-book"),
    path("books/delete/<int:pk>", BookDeleteView.as_view(), name="delete-book"),
]