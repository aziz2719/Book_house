from django.contrib import admin

from .models import Book, BookImage, Comment

admin.site.register(Book)
admin.site.register(BookImage)
admin.site.register(Comment)