from django.contrib import admin
from .models import Author, category, Book

class AuthorAdmin(admin.ModelAdmin):
    list_display=["name"]
    search_fields=["name"]

admin.site.register(Author, AuthorAdmin)

class categoryAdmin(admin.ModelAdmin):
    list_display=["name"]
    search_fields=["name"]

admin.site.register(category, categoryAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display=["name", "category", "author"]
    search_fields=["name"]

admin.site.register(Book, BookAdmin)