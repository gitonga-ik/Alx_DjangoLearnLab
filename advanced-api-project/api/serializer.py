from rest_framework import serializers
from .models import Author,Book
from django.utils import timezone

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model that converts Book instances to/from JSON.
    Includes validation to ensure publication year is not in the future.
    Attributes:
        - title: The title of the book
        - publication_year: The year the book was published (must not exceed current year)
        - author: The author of the book
    Raises:
        ValidationError: If publication_year is greater than the current year
    """
    class Meta:
        model = Book
        fields = ["title", "publication_year", "author"]

    def validate(self, book):
        if book["publication_year"] > timezone.now().year:
            raise serializers.ValidationError("Publication year cannot be in the future")
        return book
        

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.
    This serializer converts Author model instances to JSON representation and vice versa.
    It includes a nested serialization of related Book objects.
    Attributes:
        books (BookSerializer): A nested serializer that handles multiple Book instances
            associated with an Author. Set to read_only to prevent direct modification
            through this serializer.
    Meta:
        model (Author): The Author model class that this serializer is based on.
        fields (list): List of model fields to include in the serialization.
            Currently includes: 'name'
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        field = ["name"]