from django.contrib import admin
from .models import Book
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('title', 'author', 'publication_year')
    
    # Fields to search in the admin interface
    search_fields = ('title', 'author')
    
    # Fields to filter by in the admin interface
    list_filter = ('publication_year',)
    
# Register the Book model with the admin interface
admin.site.register(Book, BookAdmin) 