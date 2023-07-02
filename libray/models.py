from django.db import models
from django.contrib.auth.models import User

# Create your models here.:
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=10)
    publication_date = models.DateField()
    genre = models.CharField(max_length=50)
    availability = models.BooleanField(default=True)
    num_available = models.IntegerField(default=1)
    
class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reserved_date = models.DateTimeField(auto_now_add=True)
    is_available = models.BooleanField(default=False)
    
    
class BorrowedBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowed_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField()
    returned = models.BooleanField(default=False)
    
class WishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)
