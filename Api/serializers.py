from rest_framework.serializers import ModelSerializer
from library.models import Author, Book, category

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
        