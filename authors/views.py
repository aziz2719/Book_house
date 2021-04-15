from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from .models import Author
from .serializers import AuthorSerializer
from .permissions import IsUserOwnerOrReadOnly

class AuthorView(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    lookup_field = 'pk'
    permission_classes = (IsUserOwnerOrReadOnly, )