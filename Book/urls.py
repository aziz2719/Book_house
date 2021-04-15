"""
    2. Add a URL to urlpatterns:  path('', views.home, name='home')

    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')

    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_auth.views import LoginView
from rest_auth.registration.views import RegisterView

from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers

from users.views import UserView
from categories.views import CategoryView
from books.views import BookView
from authors.views import AuthorView

router = routers.DefaultRouter()

router.register(r'users', UserView)
router.register(r'categories', CategoryView)
router.register(r'books', BookView)
router.register(r'authors', AuthorView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signin/', LoginView.as_view(), name = 'rest_login'),
    path('signup/', RegisterView.as_view(), name = 'rest_register'),
    path('silk/', include('silk.urls', namespace='silk')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += router.urls
