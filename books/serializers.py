from rest_framework import serializers
from rest_framework.serializers import Serializer, FileField
from .models import Book, BookImage, Comment
from authors.serializers import AuthorSerializer

class BookImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookImage
        fields = ('__all__')
        

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('__all__')


class BookSerializer(serializers.ModelSerializer):
    book_images = BookImageSerializer(read_only=True, many=True)
    comment_book = CommentSerializer(read_only=True, many=True)
    author_book = AuthorSerializer(read_only=True, many=True)
    
    class Meta:
        model = Book
        fields = (
            'category', 'book_name', 'author', 'description', 'year_of_issue', 
            'price', 'rating', 'book', 'book_images', 'comment_book', 'author_book'
        )