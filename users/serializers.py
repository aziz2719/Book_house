from rest_framework import serializers
from .models import User, FavoriteBook


class FavoriteBookSerializer(serializers.ModelSerializer):

    class Meta:
        model = FavoriteBook
        fields = ('book', )


class UserSerializer(serializers.ModelSerializer):
    user_favorite_book = FavoriteBookSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = (
            'phone', 'avatar', 'username', 'first_name', 
            'last_name', 'email', 'user_favorite_book',
        )
