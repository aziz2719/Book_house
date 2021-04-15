from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView

from .models import User, FavoriteBook
from .serializers import UserSerializer, FavoriteBookSerializer
from .permissions import IsUserOwnerOrReadOnly
from books.models import Book


class UserView(ModelViewSet):
    queryset = User.objects.prefetch_related('user_favorite_book')
    serializer_class = UserSerializer
    lookup_field = 'pk'
    permission_classes = (IsUserOwnerOrReadOnly, )

class UserFavoriteBookView(APIView):

    def get(self, request, pk):
        user = User.objects.get(id=pk)
        favorite = FavoriteBook.objects.values_list('books__name', flat=True).filter(user=user)
        return Response(favorite)

class FavoriteBookView(APIView):

    def get(self, request, pk):
        user = request.user
        book = Book.objects.get(id=pk)
        favorite = FavoriteBook.objects.values_list('user__username', flat=True).filter(books=books_name)
        if Favorite.objects.filter(user=user, publication=publication).exists():
            Favorite.objects.filter(user=user, publication=publication).delete()
            return Response('FavoriteBook Deleted', status=status.HTTP_201_CREATED)
        else:
            Favorite.objects.create(user=user, publication=publication)
            return Response('FavoriteBook Created', status=status.HTTP_200_OK)