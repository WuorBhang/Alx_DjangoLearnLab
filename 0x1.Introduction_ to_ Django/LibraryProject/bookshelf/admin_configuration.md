## Configuring the Django Admin Interface for the Book Model

### Step 1: Register the Book Model with the Django Admin

In `bookshelf/admin.py`, register the `Book` model:

```python
from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author')

# Alternatively, you can use the following method to register
# admin.site.register(Book, BookAdmin)
