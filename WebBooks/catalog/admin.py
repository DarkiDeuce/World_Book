from django.contrib import admin
from .models import Author, Book, Genre, Language, Status, BookInstance

# admin.site.register(Author)
# admin.site.register(Book)
# admin.site.register(BookInstance)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    fields = ['first_name', 'last_name',
              ('date_of_birth', 'date_of_death')]

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

@admin.register(Book)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'language', 'display_author')
    list_filter = ('genre', 'author')
    inlines = [BooksInstanceInline]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'inv_nom')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )

admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Status)

