# List all books
curl http://localhost:8000/api/books/

# Create a new book
curl -X POST http://localhost:8000/api/books/ -d '{"title": "New Book", "author": "Author Name"}' -H "Content-Type: application/json"

# Retrieve a specific book
curl http://localhost:8000/api/books/1/

# Update a book
curl -X PUT http://localhost:8000/api/books/1/ -d '{"title": "Updated Book", "author": "Updated Author"}' -H "Content-Type: application/json"

# Delete a book
curl -X DELETE http://localhost:8000/api/books/1/

