from django.contrib import admin
from .models import Book, Author, Genre, Review

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ['title','summary','isbn','status']
    search_fields = ['author','title','isbn']
admin.site.register(Book, BookAdmin)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name',]
admin.site.register(Author, AuthorAdmin)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Genre, GenreAdmin)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user','book','comment','created_at']
    list_filter = ['created_at', 'user']
    search_fields = ['user','comment']
admin.site.register(Review, ReviewAdmin)
