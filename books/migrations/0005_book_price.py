# Generated by Django 3.2 on 2021-04-14 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_book_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.PositiveIntegerField(default=0, verbose_name='Цена'),
        ),
    ]
