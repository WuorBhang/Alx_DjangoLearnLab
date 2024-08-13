from django.contrib import admin
from django.urls import path, include
from relationship_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('relationship_app/', include('relationship_app.urls')),
]