from django.db import models
from django.contrib.auth.models import User

TITLE_CHOICES = (
                ("scientific",'Scientific'),
                ('religious','Religious'),
                ('psychology',"Psychology"),
                ("roman","Roman") 
                    )

class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=20)
    price = models.PositiveSmallIntegerField()
    date_added = models.DateTimeField()
    counter = models.PositiveSmallIntegerField() 
    title = models.CharField(max_length=10, choices=TITLE_CHOICES, default="psychology")

    def __str__(self):
        return f"book name is {self.name}"

class Comment(models.Model):
    body = models.CharField(max_length=200)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"commented by : {self.author} , comment : {self.body[:20]}..."
    

    
