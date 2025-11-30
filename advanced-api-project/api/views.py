from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import filters
from django_filters import rest_framework as django_filters
from .models import Book
from .serializer import BookSerializer

# Create your views here.
class BookListView(generics.ListAPIView):
    """
    A list view for retrieving Book objects with filtering, searching, and ordering capabilities.
    This view provides a read-only list endpoint for Book objects. It supports:
    - Filtering by title, author, and publication_year
    - Searching by title and author
    - Ordering by title and publication_year
    - Read-only access for unauthenticated users and full access for authenticated users
    Attributes:
        queryset: QuerySet of all Book objects
        serializer_class: BookSerializer for serializing Book data
        permission_classes: IsAuthenticatedOrReadOnly - allows read access to anyone, 
                           write access only to authenticated users
        filter_backends: DjangoFilterBackend, SearchFilter, and OrderingFilter for 
                        advanced filtering capabilities
        filterset_fields: Fields available for exact filtering (title, author, publication_year)
        search_fields: Fields available for text search (title, author)
        ordering_fields: Fields available for ordering results (title, publication_year)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [django_filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year'] 
    search_fields = ['title', 'author']      
    ordering_fields = ['title', 'publication_year']    

class BookDetailView(generics.RetrieveAPIView):
    """
    API view for retrieving the details of a single Book instance.

    This view allows authenticated users to retrieve detailed information about a specific Book object.
    Unauthenticated users have read-only access.

    Attributes:
        queryset (QuerySet): The set of Book objects to retrieve from the database.
        serializer_class (Serializer): The serializer class used to represent the Book instance.
        permission_classes (list): Permissions required to access this view. Allows authenticated users full access, and unauthenticated users read-only access.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookCreateView(generics.CreateAPIView):
    """
    API view for creating new Book instances.

    This view allows authenticated users to create new Book objects using the provided serializer.
    It inherits from Django REST Framework's CreateAPIView, which handles POST requests for object creation.

    Attributes:
        queryset (QuerySet): The set of Book objects to operate on.
        serializer_class (Serializer): The serializer class used for validating and deserializing input.
        permission_classes (list): List of permission classes; only authenticated users can access this view.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookUpdateView(generics.UpdateAPIView):
    """
    API view for updating existing Book instances.

    This view allows authenticated users to update Book objects using HTTP PUT or PATCH requests.
    Unauthenticated users have read-only access. The view uses the BookSerializer for input validation
    and serialization, and operates on all Book objects in the database.

    Attributes:
        queryset (QuerySet): All Book objects.
        serializer_class (Serializer): Serializer class for Book objects.
        permission_classes (list): Permissions required to access this view (IsAuthenticatedOrReadOnly).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookDeleteView(generics.DestroyAPIView):
    """
    API view for deleting a Book instance.

    This view allows authenticated users to delete a specific Book object.
    Unauthenticated users have read-only access and cannot perform delete operations.

    Attributes:
        queryset (QuerySet): The set of Book objects to operate on.
        serializer_class (Serializer): The serializer class for Book objects.
        permission_classes (list): Permissions required to access this view.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
