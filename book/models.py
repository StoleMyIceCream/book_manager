from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Publisher(models.Model):
    """All information about the publisher"""
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=30)
    website = models.URLField()

    def __str__(self):
        return '{!s}'.format(self.name)


class Author(models.Model):
    """All information about for Author"""
    salutation = models.CharField(max_length=10)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return '{!s} {!s}'.format(self.first_name,
                                  self.last_name,)


class Book(models.Model):
    """All information about for Book"""
    title = models.CharField(max_length=100)
    authors = models.ForeignKey(Author, default=0)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()
    num_pages = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return '{!s}'.format(self.title,)
