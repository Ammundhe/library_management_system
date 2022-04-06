from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.viewsets import ModelViewSet
from Api.serializers import Author_serializer, Book_serializer, category_serializer, Department_serializer, student_serializer, Issue_serializer
from library.models import Author, Book, category, Issue
from student.models import student, Department


class LoginPage(ObtainAuthToken):
    renderer_classes=api_settings.DEFAULT_RENDERER_CLASSES


class author(ModelViewSet):
    serializer_class=Author_serializer
    queryset= Author.objects.all()

class Category(ModelViewSet):
    serializer_class=category_serializer
    queryset=category.objects.all()

class book(ModelViewSet):
    serializer_class=Book_serializer
    queryset=Book.objects.all()

class Student(ModelViewSet):
    serializer_class=student_serializer
    queryset=student.objects.all()

class department(ModelViewSet):
    serializer_class=Department_serializer
    queryset=Department.objects.all()

class issue(ModelViewSet):
    serializer_class=Issue_serializer
    queryset=Issue.objects.all()
