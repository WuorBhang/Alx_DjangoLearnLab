from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser
from django.contrib.auth.models import Group, Permission
from .models import Document




class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by')

admin.site.register(Document, DocumentAdmin)

admin.site.register(CustomUser, CustomUserAdmin)

# Register your models here.

admin.site.register(Book, BookAdmin)
