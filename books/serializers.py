from rest_framework import serializers
from .models import Book


class BookSerializer(serializers. HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ('url', 'id', 'book_name', 'author', 'published_date', 'no_of_pages', 'rack_number')