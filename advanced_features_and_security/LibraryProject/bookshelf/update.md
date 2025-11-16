# Update Operation
- Command to update a given book instance in your db using the django shell
## Command
```python
update_book = Book.objects.get(title="1984")
update_book.title = "Nineteen Eighty-Four"
update_book.save()
update_book.title
```

# Output
"Nineteen Eighty-Four"