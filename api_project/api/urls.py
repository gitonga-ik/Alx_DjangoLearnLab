from django.urls import path,include
from .views import BookList, BookViewSet
from rest_framework import router
from rest_framework.authtoken import views

router = router.DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  
    path('get-token', views.obtain_auth_token, name='auth-token'),
    path('', include(router.urls))
]