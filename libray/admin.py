from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Book,Reservation,BorrowedBook,WishList
# from . managers import User

# Register your models here.
admin.site.register(Book)
admin.site.register(Reservation)
admin.site.register(BorrowedBook)
admin.site.register(WishList)
