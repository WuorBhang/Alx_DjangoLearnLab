from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author = Author.objects.get(name="Author Name")
books_by_author = Book.objects.filter(author=author)
print(f"Books by {author.name}:")
for book in books_by_author:
    print(book.title)

# List all books in a library
library = Library.objects.get(name="Library Name")
books_in_library = library.books.all()
print(f"Books in {library.name}:")
for book in books_in_library:
    print(book.title)

# Retrieve the librarian for a library
library = Library.objects.get(name="Library Name")
librarian = Librarian.objects.get(library=library)
print(f"Librarian for {library.name}: {librarian.name}")
