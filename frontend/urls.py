from django import views
from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePage.as_view(), name="HomePage"),
    path("book-listing", views.BookCategories.as_view(), name="BookCategories"),
    path("book-listing/<int:bookId>", views.BookCategories.as_view(), name="BookCategories"),
    path("student-list", views.Student.as_view(), name="Student"),
    path("student-list/<int:student_id>", views.Student.as_view(), name="Student"),
    path("issue-details", views.IssueDetails.as_view(), name="IssueDetails"),    
    path("issued-books", views.IssueBooks.as_view(), name="IssueBooks"),    
]
