from .models import Author, Book, Library, Librarian

def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    print(f"Books by {author_name}:")
    for book in books:
        print(f"- {book.title}")

def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    print(f"Books in the library {library_name}:")
    for book in books:
        print(f"- {book.title}")

def librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)
    print(f"The librarian for {library_name} is {librarian.name}")

if __name__ == "__main__":
    books_by_author('Author Name')
    books_in_library('Library Name')
    librarian_for_library('Library Name')
    