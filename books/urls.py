from django.urls import path
from . import views

app_name = "books"

urlpatterns = [
    path('', views.index, name="index" ),
    path('books/', views.books, name="book" ),
    path('book/<int:book_id>/', views.book, name="book_detail"),
    path('book/<slug:mode>/', views.filter_mode, name="filter_mode"),
   


]