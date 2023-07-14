from django.urls import path
from bookstore import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-to-cart/<int:book_id>/', views.add_to_cart, name='add-to-cart'),
    path('get-books/', views.get_books, name='get-books'),
    path('books/<int:book_id>', views.get_book_details, name='book-details'),
    path('cart', views.get_cart, name='cart'),
    path('cart/remove/<int:book_id>', views.remove_from_cart, name='remove-from-cart'),
    path('books/create/', views.create_book, name='create_book'),
]
