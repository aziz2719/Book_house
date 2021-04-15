from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from .models import Book, BookImage, Comment
from .serializers import BookSerializer, BookImageSerializer, CommentSerializer
from .permissions import IsUserOwnerOrReadOnly, IsCommentsOwnerOrReadOnly

from rest_framework.permissions import IsAuthenticated

class BookView(ModelViewSet):
    queryset = Book.objects.prefetch_related('book_images', 'comment_book')
    serializer_class = BookSerializer
    lookup_field = 'pk'
    permission_classes = (IsUserOwnerOrReadOnly, )

class BookImageView(ModelViewSet):
    queryset = BookImage.objects.all()
    serializer_class = BookImageSerializer
    lookup_field = 'pk'
    permission_classes = (IsUserOwnerOrReadOnly, )

class CommentView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'pk'
    permission_classes = (IsCommentsOwnerOrReadOnly, IsAuthenticated, )

