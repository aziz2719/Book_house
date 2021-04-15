from django.contrib import admin

from .models import User, FavoriteBook


admin.site.register(User)
admin.site.register(FavoriteBook)