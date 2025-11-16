# Create Operation

## Command
```python
new_book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
```

# Retrieve Operation

## Command
```python
retrieve_book = Book.objects.get(title="1984")
retrieve_book.title
```

## Output
```python
1984
```

# Update Operation

## Command
```python
update_book = Book.objects.get(title="1984")
update_book.title = "Nineteen Eighty-Four"
update_book.save()
update_book.title
```

# Output
"Nineteen Eighty-Four"

# Delete Operation

## Command
```python
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
(1, {'bookshelf.Book': 1})
books = Book.objects.all()
books
```
## Output
<QuerySet []>