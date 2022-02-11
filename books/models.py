from django.db import models


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

