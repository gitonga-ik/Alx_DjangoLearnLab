from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="relationship_app/login.html"),
        name="user-login",
    ),
    path("logout/", views.logout_user, name="user-logout"),
    path("register/", views.register_user, name="register"),
    path("book-list/", views.book_list, name="book-list"),
    path("library-details/", views.LibraryList.as_view(), name="library-details"),
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
]
