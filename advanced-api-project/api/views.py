from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from .models import Book
from .serializers import BookSerializer



# BookListView
class BookListView(generics.ListCreateAPIView):
    # View to list all books or create a new book.
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Public access for listing books

    def perform_create(self, serializer):
        # Custom method to handle book creation.
        serializer.save()  # Save the new book instance with additional logic if needed

# BookDetailsView
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    # View to retrieve, update, or delete a book.
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only allow authenticated users to modify or delete books

    def perform_update(self, serializer):
        # Custom method to handle book updates.
        serializer.save()  # Save the updated book instance

    def perform_destroy(self, instance):
        # Custom method to handle book deletion.
        instance.delete()  # Delete the book instance