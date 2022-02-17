from django.contrib import admin
from .models import Book, Comment, Image, RequestBook

#admin.site.register(Book)
admin.site.register(RequestBook)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("name","author","price","title")
    list_filter = ('name','author','title')
    search_fields = ('name','author','title')
    ordering = ('name','author','title')
    date_hierarchy = 'date_added'
    row_id_fields = ('author',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('body','book','author','date_added')
    list_filter = ('book','author','date_added')
    search_fields = ('body','book','author','date_added')

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('title','book')
    list_filter = ('title','book')
    search_fields = ('title','book')

