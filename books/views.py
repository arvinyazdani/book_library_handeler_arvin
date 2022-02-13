from django.shortcuts import render, redirect
from .models import Book
from .forms import CommentForm
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'book/index.html')

@login_required
def books(request):
    book = Book.objects.order_by("-date_added")
    context = {"book":book}
    return render(request, 'book/books.html', context)

@login_required
def book(request,book_id):
    book = Book.objects.get(id=book_id)
    comments = book.comment_set.order_by("-date_added")
    if request.method != "POST":
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST)
        if form.is_valid():
            add_user = form.save(commit=False)
            add_user.author = request.user
            add_user.book = book
            add_user.save()
            return redirect("books:book_detail",book_id)

    
    context = {"book":book,"comments":comments, "form":form}
    return render(request, "book/book_detail.html", context)