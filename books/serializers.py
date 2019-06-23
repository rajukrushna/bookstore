from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    book_name = serializers.CharField(required=True, max_length=100)
    author = serializers.CharField(required=True, max_length=100)
    published_date = serializers.DateField(required=True)
    no_of_pages = serializers.IntegerField(required=True)
    rack_number = serializers.IntegerField(required=True)

    def create(self, validated_data):
        """
        Create and return a new 'Book' instance, given the validated data
        """
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing Book instance, given the validated data
        """
        instance.book_name = validated_data.get('book_name', instance.book_name)
        instance.author = validated_data.get('author', instance.author)
        instance.published_date = validated_data.get('published_date', instance.published_date)
        instance.no_of_pages = validated_data.get('no_of_pages', instance.no_of_pages)
        instance.rack_number = validated_data.get('rack_number', instance.rack_number)
        instance.save()
        return instance
