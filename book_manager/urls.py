"""book_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from book import views
from book.views import bookview, authorview, publisherview

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.homepage, name='homepage'),
    url(r'^books/$', bookview.as_view(), name='books'),
    url(r'^books/(?P<book_id>\d+)/$', views.book_detail, name='book_detail'),
    url(r'^authors/$', authorview.as_view(), name='authors'),
    url(r'^authors/(?P<author_id>\d+)/$', views.author_detail,
        name='author_detail'),
    url(r'^publisher/$', publisherview.as_view(), name='publisher'),
    url(r'^publisher/(?P<publisher_id>\d+)/$', views.publisher_detail,
        name='publisher_detail'),
    url(r'^search/$', views.search, name='search'),
    url(r'^search/(?P<book_id>\d+)/$', views.book_detail, name='book_detail'),
]
