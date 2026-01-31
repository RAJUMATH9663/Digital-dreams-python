from django.shortcuts import render, redirect
from .models import Book, Student, Issue

def home(request):
    books = Book.objects.all()
    return render(request, 'home.html', {'books': books})


def add_book(request):
    if request.method == "POST":
        Book.objects.create(
            title=request.POST['title'],
            author=request.POST['author'],
            isbn=request.POST['isbn']
        )
        return redirect('/')
    return render(request, 'add_book.html')


def add_student(request):
    if request.method == "POST":
        Student.objects.create(
            name=request.POST['name'],
            email=request.POST['email']
        )
        return redirect('/')
    return render(request, 'add_student.html')


def issue_book(request):
    if request.method == "POST":
        student = Student.objects.get(id=request.POST['student'])
        book = Book.objects.get(id=request.POST['book'])

        Issue.objects.create(student=student, book=book)
        book.available = False
        book.save()

        return redirect('/')

    students = Student.objects.all()
    books = Book.objects.filter(available=True)
    return render(request, 'issue.html', {
        'students': students,
        'books': books
    })


def return_book(request, id):
    issue = Issue.objects.get(id=id)
    issue.book.available = True
    issue.book.save()
    issue.return_date = "2025-01-01"
    issue.save()

    return redirect('/')