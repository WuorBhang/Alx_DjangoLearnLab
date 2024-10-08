# Alx_DjangoLearnLab
# Django Permissions Setup

## Custom Permissions
- `can_view`: Allows viewing articles.
- `can_create`: Allows creating articles.
- `can_edit`: Allows editing articles.
- `can_delete`: Allows deleting articles.

## User Groups
- **Editors**: Can create and edit articles.
- **Viewers**: Can only view articles.
- **Admins**: Can perform all actions (view, create, edit, delete).

## Usage
- Use the `@permission_required` decorator in views to enforce permissions.
- Manage groups and permissions through the Django admin interface.
