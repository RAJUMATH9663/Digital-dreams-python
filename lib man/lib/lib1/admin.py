from django.contrib import admin
from .models import Student, Book, Issue

admin.site.register(Student)
admin.site.register(Book)
admin.site.register(Issue)