from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from .models import Author, Book

class AuthorResource(resources.ModelResource):
    class Meta:
        model = Author
        fields = ("id", "first_name", "last_name")

class BookResource(resources.ModelResource):
    author = fields.Field(
        column_name='author',
        attribute='author',
        widget=ForeignKeyWidget(Author, 'id')  # or 'first_name' if you want
    )

    class Meta:
        model = Book
        fields = ("id", "author", "title", "description", "created_at")
        export_order = ("id", "author", "title", "description", "created_at")