from django.contrib import admin

from .models import LibrarianDb, Books,IssueReturn

admin.site.register(LibrarianDb)
admin.site.register(Books)
admin.site.register(IssueReturn)
