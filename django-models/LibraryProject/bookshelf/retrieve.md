# Retrieve Operation
- Command to retrieve book instances from your db using the django shell

## Command
```python
retrieve_book = Book.objects.get(title="1984")
retrieve_book.title
```

## Output
```python
1984
```