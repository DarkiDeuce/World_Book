from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Author, BookInstance, Genre
from django.views import generic
from django.template.loader import render_to_string
from django.contrib.auth.mixins import LoginRequiredMixin

def index(requst):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact=2).count()
    num_authors = Author.objects.count()
    num_visits = requst.session.get('num_visits', 0)
    requst.session['num_visits'] = num_visits + 1

    return render(requst, 'index.html', context={'num_books': num_books,
                                                 'num_instances': num_instances,
                                                 'num_instances_available': num_instances_available,
                                                 'num_authors': num_authors,
                                                 'num_visits': num_visits,}
                  )

class BookListView(generic.ListView):
    model = Book
    paginate_by = 3

class BookDetailView(generic.DetailView):
    model = Book

class AuthorsListView(generic.ListView):
    model = Author
    paginate_by = 4

class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='2').order_by('due_back')