from django.db import models
from django.contrib.auth.models import User

TITLE_CHOICES = (
                ("scientific",'Scientific'),
                ('religious','Religious'),
                ('psychology',"Psychology"),
                ("roman","Roman") 
                    )

STATUS_CHOICES = (
                ("basy",'Basy'),
                ('free','Free'))

class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=20)
    price = models.PositiveSmallIntegerField()
    date_added = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="free")
    title = models.CharField(max_length=10, choices=TITLE_CHOICES, default="psychology")
    basy_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    basy_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    body = models.CharField(max_length=200)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.body
    

    
class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to=f'media/images/%Y/%m/%d/',blank=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)


    def __str__(self):
        return self.title






        