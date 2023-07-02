from django.urls import path
from .import views

urlpatterns = [
    path('book/search/', views.book_search, name='book_search'),
    path('book/reserve/<int:book_id>/', views.reserve_book, name='reserve_book'),
    path('book/borrow/<int:book_id>/', views.borrow_book, name='borrow_book'),
    path('book/return/<int:book_id>/', views.return_book, name='return_book'),
    path('book/wishlist/add/<int:book_id>/', views.add_to_wishlist, name='add_to_wishlist'),
]
