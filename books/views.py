from .models import Book
from .serializers import BookSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from .permissions import IsAdminOrReadOnly
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly


@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticatedOrReadOnly, IsAdminOrReadOnly,))
def book_list(request, format=None):
    """
    List all books or add a new book
    """
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticatedOrReadOnly, IsAdminOrReadOnly,))
def book_detail(request, pk, format=None):
    """
    Retrieve, update or delete a book
    """
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
