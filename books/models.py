from django.db import models


class Book(models.Model):
    book_name = models.CharField(unique=True, max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    no_of_pages = models.IntegerField()
    rack_number = models.IntegerField()

    class Meta:
        ordering = ('book_name',)
