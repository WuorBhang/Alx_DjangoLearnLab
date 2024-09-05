from rest_framework import serializers
from .models import Author, Book




# Serializer for the Book model, including validation for publication year.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        if value > 2024:  # Current year
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


# Serializer for the Author model.
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']
