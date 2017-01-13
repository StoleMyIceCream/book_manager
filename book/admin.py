from django.contrib import admin
from models import Book, Author, Publisher
# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publication_date')
    ordering = ('publisher', 'publication_date')
    search_fields = ('title',)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    list_filter = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')


class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'website')
    list_filter = ('name', 'country')
    search_fields = ('name',)


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher, PublisherAdmin)
