# Create Operation
- Command to create a new book instance using the django shell
- Fleds required are title, author and year of publication

## Command
```python
new_book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
```
- The book is created successfully and returns a Book instance
- No explicit output is shown in the shell, but the object is created in the database
