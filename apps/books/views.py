from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Book, Review
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import ReviewForm
from django.contrib.auth.models import User

# Create your views here.
app_name = 'books'

class BookListView(generic.ListView):
    # model = Book
    template_name="books/book/book_list.html"
    context_object_name = 'all_books'
    section = 'books'
    queryset = Book.objects.filter(status='approved')
    paginate_by = 2
    # def get_queryset(self):
    #     live_entries = Book.objects.filter(status='approved')
    #     # return Book.objects.all()
    #     return live_entries

class BookDetailView(generic.DetailView):
    model = Book
    template_name="books/book/book_detail.html"
class BookCreate(CreateView):
    model = Book
    template_name="books/book/book_add.html"
    fields = ['author','title','summary','isbn','genre']

def add_review(request,pk):
    book = get_object_or_404(Book,pk=pk)
    review_form = ReviewForm()
    if request.method == 'POST':
        if review_form.is_valid():
            review_form = ReviewForm(request.POST)
            # review = Review.objects.get(id=pk)
            # comment = review_form['comment']
            comment = form.cleaned_data['comment']
            review = Review()
            review.user = request.user
            review.comment = comment
            review.created_at = datetime.datetime.now()
            review.save()

        return HttpResponseRedirect(reverse('books:book-detail',args=(pk,)))

    return render(request,'books/book/review_add.html',{'review_form':review_form})

def book_search(request):
    pass
