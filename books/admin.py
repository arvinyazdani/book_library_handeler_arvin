from django.contrib import admin
from .models import Book, Comment, Image

admin.site.register(Book)
admin.site.register(Comment)
admin.site.register(Image)
