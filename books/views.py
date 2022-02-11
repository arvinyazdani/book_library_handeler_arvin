from django.shortcuts import render
from .models import Book

def index(request):
    return render(request, 'book/index.html')

def books(request):
    book = Book.objects.all()
    context = {"book":book}
    return render(request, 'book/books.html', context)