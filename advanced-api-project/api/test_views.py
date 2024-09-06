from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from .models import Book
from django.contrib.auth.models import User


class BookAPITest(APITestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = APIClient()

        # Create some Book instances
        self.book1 = Book.objects.create(title='Book 1', author='Author 2', publication_year=2000)
        self.book2 = Book.objects.create(title='Book 2', author='Author 2', publication_year=2020)

    def test_list_books(self):
        # Test listing all books.
        url = reverse('book-list')  # Assuming 'book-list' is the name of your URL for BookListView
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Should return 2 books

    def test_create_book(self):
        # Test creating a new book.
        self.client.login(username='testuser', password='testpassword')  # Authenticated request
        url = reverse('book-create')
        data = {
            'title': 'New Book',
            'author': 'New Author',
            'publication_year': 2022
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)  # Now 3 books in total

    def test_update_book(self):
        # Test updating an existing book.
        self.client.login(username='testuser', password='testpassword')  # Authenticated request
        url = reverse('book-update', kwargs={'pk': self.book1.pk})
        data = {'title': 'Updated Book 1'}
        response = self.client.put(url, data, format='json')
        self.book1.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.book1.title, 'Updated Book 1')

    def test_delete_book(self):
        # Test deleting a book.
        self.client.login(username='testuser', password='testpassword')  # Authenticated request
        url = reverse('book-delete', kwargs={'pk': self.book2.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)  # Only 1 book should remain

    def test_filter_books(self):
        # Test filtering books by title.
        url = reverse('book-list') + '?title=Book 1'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Book 1')

    def test_search_books(self):
        # Test searching for books by author.
        url = reverse('book-list') + '?search=Author 2'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['author'], 'Author 2')

    def test_order_books(self):
        # Test ordering books by publication year.
        url = reverse('book-list') + '?ordering=publication_year'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Book 1')  # Book 1 was published earlier
