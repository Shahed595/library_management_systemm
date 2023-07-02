from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . models import Book, Reservation, BorrowedBook, WishList

# Create your views here.
# def book(request):
    

def book_search(request):
    if request.method == 'GET':
        query = Book.objects.all()
        # books = Book.objects.filter(title__icontains=query)
        return render(request, 'library/book_search.html', {'books':query})
    
def reserve_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if book.availability and book.num_available > 0:
        reservation = Reservation(user = request.user, book=book, is_available=True)
        reservation.save()
        book.num_available-=1
        book.save()
        messages.success(request, 'Book reserved successfully!')
    else:
        messages.error(request, 'Book is currently unavailable for reservation!')
    return redirect ('book_search')

def borrow_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if book.availability and book.num_available > 0:
        borrowed_book = BorrowedBook(user = request.user, book=book, due_date = calculate_due_date())
        borrow_book.save()
        book.num_available-=1
        book.save()
        messages.success(request, 'Book borrowed successfully!')
    else:
        messages.error(request, 'Book is currently unavailable for borrowing.')
    return redirect('book_search')

def return_book(request, book_id):
    borrowed_book = BorrowedBook.objects.get(user=request.user, book_id=book_id, returned=False)
    borrowed_book.returned = True
    borrowed_book.save()
    book = Book.objects.get(id = book_id)
    book.num_available+=1
    book.save()
    messages.success(request, 'Book returned successfully!')
    return redirect('book_search')

def add_to_wishlist(request, book_id):
    book = Book.objects.get(id=book_id)
    wishlist = WishList(user = request.user, book=book)
    wishlist.save()
    messages.success(request, 'Book added to wishlist!')
    return redirect('book_search')

def calculate_due_date():
    pass





