from django.db import models
from django.contrib.auth.models import User

from .utils import object_statuses, reading_statuses


class Author(models.Model):
    fname = models.CharField(verbose_name="first name", max_length=32)
    mname = models.CharField(verbose_name="middle name", max_length=32, blank=True, null=True)
    lname = models.CharField(verbose_name="last name", max_length=32, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=False)
    status = models.CharField(choices=object_statuses, max_length=10, blank=True, null=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('created_on',)

    def __str__(self):
        s = self.fname
        if self.mname:
            s+= f" {self.mname}"
        if self.lname:
            s+= f" {self.lname}"
        return s


class Tag(models.Model):
    value = models.CharField(max_length=32)
    slug = models.SlugField(unique=True, blank=True, null=False)
    status = models.CharField(choices=object_statuses, max_length=10, blank=True, null=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

class Book(models.Model):
    name = models.CharField(max_length=64)
    author = models.ManyToManyField(Author, blank=True)
    tags    = models.ManyToManyField(Tag)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=False)
    status = models.CharField(choices=object_statuses, max_length=10, blank=True, null=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    

class BookReading(models.Model):
    """copies of owner and book's names are stored because of data analysis"""
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    status = models.CharField(choices=object_statuses, max_length=10, blank=True, null=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.owner} - {self.book}"


class ReadingStatus(models.Model):
    """all statuses are kept. only new ones are active."""
    reading = models.ForeignKey(BookReading, on_delete=models.SET_NULL, null=True, blank=False)
    book_name = models.CharField(max_length=64, blank=True, null=True)
    current_status = models.CharField(choices=reading_statuses, max_length=16, blank=True, null=False)
    status = models.CharField(choices=object_statuses, max_length=10, blank=True, null=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.current_status}: {self.book_name}"
