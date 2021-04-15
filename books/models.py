from django.db import models

class Book(models.Model):
    category = models.ForeignKey('categories.Category', models.CASCADE, 'category_book', null=True)
    book_name = models.CharField('Название книги', max_length=255)
    author = models.ForeignKey('authors.Author', models.SET_NULL, 'author_book', null=True)
    description = models.TextField('Описание')
    year_of_issue = models.CharField('Год выпуска', max_length=20)
    price = models.PositiveIntegerField('Цена', default=0)
    rating = models.FloatField('Рейтинг', default=0, max_length=1)
    book = models.FileField('Книга', upload_to='books/')
    
    def __str__(self):
        return self.book_name


class BookImage(models.Model):
    book = models.ForeignKey('books.Book', models.CASCADE, 'book_images')
    image = models.ImageField('Фото', upload_to='book_images')


class Comment(models.Model):
    book = models.ForeignKey('books.Book', models.SET_NULL, 'comment_book', null=True)
    user = models.ForeignKey('users.User', models.SET_NULL, 'user_comment', null=True)
    comment = models.TextField('Коментарий')
    mark = models.FloatField('Оценка', default=0, max_length=1)
    created_at = models.DateTimeField('Дата и время создания', auto_now_add=True, null=True)

    def __str__(self):
        return self.comment