# Book API In Advanced_API_project

This API provides the following endpoints to manage books:

1. **List all books**: `GET /books/`
2. **Retrieve a single book**: `GET /books/<id>/`
3. **Create a book**: `POST /books/create/` (authenticated users only)
4. **Update a book**: `PUT /books/<id>/update/` (authenticated users only)
5. **Delete a book**: `DELETE /books/<id>/delete/` (authenticated users only)

## Custom Permissions
- Unauthenticated users can view books but cannot modify them.
- Only authenticated users can create, update, or delete books.
