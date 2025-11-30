from django.db import models

# Create your models here.
class Author(models.Model):
    """
    Author model representing a writer or content creator.

    Attributes:
        name (CharField): The name of the author, with a maximum length of 200 characters.
    """
    name = models.CharField(max_length=200)

class Book(models.Model):
    """
    Book model representing a published book in the library system.

    Attributes:
        title (CharField): The title of the book, max length 200 characters.
        publication_year (IntegerField): The year the book was published.
        author (ForeignKey): A reference to the Author of the book. 
                             Deletes the book if the associated author is deleted (CASCADE).
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)