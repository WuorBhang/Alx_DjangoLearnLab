from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser
from django.contrib.auth.models import Group, Permission
from .models import Document

class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by')

admin.site.register(Document, DocumentAdmin)



class CustomUserAdmin(BaseUserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm  # Create this form for user creation
    form = CustomUserChangeForm  # Create this form for user changes

    list_display = ('email', 'username', 'date_of_birth', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions', 'groups')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'date_of_birth', 'profile_photo', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)

# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author')

# Alternatively, you can use the following method to register
# admin.site.register(Book, BookAdmin)
