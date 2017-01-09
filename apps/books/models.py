from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.core.validators import RegexValidator
from django.core.urlresolvers import reverse


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return ('{}, {}').format(self.last_name,self.first_name)


class Genre(models.Model):
    name = models.CharField(max_length=200, help_text="Enter a book genre(e.g. Science Fiction, French, Poetry, etc.)")

    def __str__(self):
        return self.name
        # ^string for representing the Model object (in Admin site etc.)

# class BookManager(models.Manager):
#     def add_book(self,author,title,summary,isbn,genre):
#         book = self.create(title=title, author=author, summary=summary, isbn=isbn, genre=genre)
# # book = Book.objects.add_book("Pride and Prejudice")
class Book(models.Model):
    STATUS_CHOICES = (
        ('pending','Pending'),
        ('approved','Approved'),
        ('hidden','Hidden')
    )
    author = models.ManyToManyField(Author)
    # photo = models.ImageField(upload_to='books/<book.pk>/%Y/%m/%d', default=None,blank=True)
    title = models.CharField(max_length=100)
    summary = models.TextField(max_length=3000,help_text="Enter a brief description of the book")
    isbn = models.CharField(validators=[RegexValidator(regex='^.{13}$', message='Length has to be 13', code='nomatch')],max_length=13, unique=True)
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='pending')
    # objects = BookManager()
    def get_absolute_url(self):
        return reverse('books:book-detail', kwargs={'pk':self.pk})

    class Meta:
        ordering = ('-updated_at',)

    def __str__(self):
        return self.title

class Review(models.Model):
    user = models.ForeignKey(User,related_name='user_reviews')
    book = models.ForeignKey(Book,related_name='book_reviews')
    comment = models.CharField(max_length=3000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['created_at']
    def __str__(self):
        return self.comment
    def get_poster_info(self):
        return "Review by {} on {}".format(self.user, self.created_at)
    def recent_posts_by_user(self):
        pass
    def review_count(self):
        pass


    def __str__(self):
        return 'Comment  by {} on {}'.format(self.user,self.created_at)
