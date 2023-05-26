from django.contrib import admin
from .models import Author

REGISTER = admin.site.register

REGISTER(Author)
