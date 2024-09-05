from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),  # List
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),  # Retrieve, 
    path('books/create/', BookCreateView.as_view(), name='book-create'), # create books,
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'), # update,
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'), # delete a specific book, 
]