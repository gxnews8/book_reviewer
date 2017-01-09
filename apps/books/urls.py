from django.conf.urls import url, include
from . import views
from views import BookListView, BookDetailView,BookCreate
app_name = 'books'
urlpatterns = [
    url(r'^$', BookListView.as_view(),name="books-list"),
    url(r'^(?P<pk>[0-9]+)/$', BookDetailView.as_view(), name="book-detail"),
    url(r'^(?P<pk>[0-9]+)/review/add/$', views.add_review, name="add-review"),
    url(r'^add/$', BookCreate.as_view(),name="book-add"),

]
