from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Author, Book
from .resources import AuthorResource, BookResource

# Register your models here.


@admin.register(Author)
class AuthorAdmin(ImportExportModelAdmin):
    resource_class = AuthorResource
    list_display = ('id', 'first_name', 'last_name')
    search_fields = ('first_name', 'last_name')


@admin.register(Book)
class BookAdmin(ImportExportModelAdmin):
    resource_class = BookResource
    list_display = ('id', 'title', 'author', 'created_at')
    search_fields = ('title', 'author__first_name', 'author__last_name')
    list_filter = ('created_at', 'author')

