from django.db.models import Q
from django.shortcuts import render, render_to_response, get_object_or_404
from django.views.generic.list import ListView

from models import Book, Author, Publisher


# Create your views here
def homepage(request):
    return render(request, 'homepage.html')


class bookview(ListView):
    """docstring for bookview"""
    model = Book

    def get_context_data(self, **kwargs):
        context = super(bookview, self).get_context_data(**kwargs)
        return context


class authorview(ListView):
    """docstring for authorview"""
    model = Author

    def get_context_data(self, **kwargs):
        context = super(authorview, self).get_context_data(**kwargs)
        return context


class publisherview(ListView):
    """docstring for publisherview"""
    model = Publisher

    def get_context_data(self, **kwargs):
        context = super(publisherview, self).get_context_data(**kwargs)
        return context


def book_detail(request, book_id):
    book_detail = get_object_or_404(Book.objects.filter(id=book_id))
    return render(request, "book/book_details.html",
                  {'details': book_detail})


def author_detail(request, author_id):
    author_detail = get_object_or_404(Author.objects.filter(id=author_id))
    return render(request, "book/author_details.html",
                  {'details': author_detail})


def publisher_detail(request, publisher_id):
    publisher_detail = get_object_or_404(Publisher.objects.filter(id=publisher_id))
    return render(request, "book/publisher_details.html",
                  {'details': publisher_detail})


def search(request):
    query = request.GET.get('q', '')
    query_author = request.GET.get('q', '')
    if query:
        qset = (Q(title__icontains=query) |
                Q(authors__first_name__icontains=query) |
                Q(authors__last_name__icontains=query)
                )
        qset_author = (Q(first_name__icontains=query_author) |
                       Q(last_name__icontains=query_author)
                       )
        results = Book.objects.filter(qset).distinct()
        results_author = Author.objects.filter(qset_author)
    else:
        results = []
    return render_to_response("book/search.html", {"results": results,
                                                   "results_author": results_author,
                                                   "query": query})
