# Delete Operation
- Command to delete a given book instance in your db using the django shell

## Command
```python
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
(1, {'bookshelf.Book': 1})
books = Book.objects.all()
books
```
## Output
<QuerySet []>