from django.db import models

class Author(models.Model):
    # The name of the author
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    # The title of the book
    title = models.CharField(max_length=200)
    # The year the book was published
    publication_year = models.IntegerField()
    # The author of the book, establishing a one-to-many relationship
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title