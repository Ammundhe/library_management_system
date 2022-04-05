from rest_framework.serializers import ModelSerializer
from library.models import Author, Book, category, Issue
from student.models import student, Department

class Author_serializer(ModelSerializer):
    class Meta:
        model=Author
        fields="__all__"
class Book_serializer(ModelSerializer):
    class Meta:
        model=Book
        fields="__all__"
class category_serializer(ModelSerializer):
    class Meta:
        model=category
        fields="__all__"
        
class student_serializer(ModelSerializer):
    class Meta:
        model=student
        fields="__all__"
        
class Department_serializer(ModelSerializer):
    class Meta:
        model=Department
        fields="__all__"

class Issue_serializer(ModelSerializer):
    class Meta:
        model=Issue
        fields="__all__"
        