# Social Media API

## Project Setup

1. Clone the repository:
   git clone https://github.com/Alx_Djangolab/WuorBhang/social_media_api.git

   cd social_media_api

Install dependencies:
pip install -r requirements.txt


Run migrations:
python manage.py makemigrations
python manage.py migrate

Start the server:
python manage.py runserver


API Endpoints
Register: POST /api/accounts/register/

Body: { "username": "testuser", "password": "password123", "email": "user@example.com" }
Login: POST /api/accounts/login/

Body: { "username": "testuser", "password": "password123" }
Profile: GET /api/accounts/profile/

Header: Authorization: Token <My/Your_token>


User Model
The custom user model includes additional fields like:
    bio: A brief bio for the user.
    profile_picture: A user profile image.
    followers: A many-to-many field representing user followers.