from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookForm
from django.http import HttpResponse
from .models import Book
from django.core.paginator import Paginator


# def home(request):
#     books = Book.objects.all()  # get all books from DB
#     return render(request, 'home.html', {'books': books})
def home(request):
    book_list = Book.objects.all().order_by('id')  # get all books
    paginator = Paginator(book_list, 5)  # 5 books per page

    page_number = request.GET.get('page')  # get page number from URL ?page=
    page_obj = paginator.get_page(page_number)  # get the books for that page

    return render(request, 'home.html', {'page_obj': page_obj})

def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new book to DB
            return redirect('home')  # after saving, go to homepage
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

def edit_book(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm(instance=book)
    return render(request, 'edit_book.html', {'form': form})

def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('home')  # go back to homepage after deletion
