from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from Api.serializers import Author_serializer, Book_serializer, category_serializer
from library.models import Author, Book, category


class author(ModelViewSet):
    serializer_class=Author_serializer
    queryset= Author.objects.all()

class Category(ModelViewSet):
    serializer_class=category_serializer
    queryset=category.objects.all()

class book(ModelViewSet):
    serializer_class=Book_serializer
    queryset=Book.objects.all()
