from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.models import User

def register(request):
    if request.method != "POST":   
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('books:index')
    context = {"form":form}
    return render(request, "registration/register.html", context)

def profile(request, user_id):
    user =   User.objects.get(id=user_id)
    books = user.book_set.all().order_by("-basy_date")

    context = {"user":user,"books":books}

    return render(request, "profile.html", context)








