from api.models import Author, Book
from api.serializers import AuthorSerializer, BookSerializer

author = Author.objects.create(name="J.K. Rowling")
book = Book.objects.create(title="Harry Potter", publication_year=1997, author=author)

author_serializer = AuthorSerializer(author)
print(author_serializer.data)

