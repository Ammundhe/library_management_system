from django.contrib import admin
from library.models import Author, category, Book, Issue

class AuthorAdmin(admin.ModelAdmin):
    list_display=["name"]
    search_fields=["name"]
admin.site.register(Author, AuthorAdmin)

class categoryAdmin(admin.ModelAdmin):
    list_display=["name"]
    search_fields=["name"]
admin.site.register(category, categoryAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display=["name", "author", "category"]
    list_filter=["category", "author"]
    search_fields=["name"]

admin.site.register(Book, BookAdmin)

class IssueAdmin(admin.ModelAdmin):
    list_display=["student", "book", "issued", "issued_at", "created_at", "returned", "return_date"]
    list_filter=["issued", "returned"]
    search_fields=["student"]
admin.site.register(Issue, IssueAdmin)
