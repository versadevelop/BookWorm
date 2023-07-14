from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Book, CartItem, BookForm


def get_books(request):
    sort_by = request.GET.get('sort_by', 'price')
    reverse = request.GET.get('reverse', 'false').lower() == 'true'

    books = Book.objects.order_by(sort_by)
    if reverse:
        books = books.reverse()

    data = [
        {
            'id': book.id,
            'title': book.title,
            'author': book.author,
            'price': str(book.price),
            'description': book.description
        }
        for book in books
    ]

    return JsonResponse(data, safe=False)


def get_book_details(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    data = {'id': book.id, 'title': book.title, 'author': book.author,
            'price': str(book.price), 'description': book.description}

    return JsonResponse(data)


def get_cart(request):
    cart_items = CartItem.objects.all()
    data = [{'book': {'id': item.book.id, 'title': item.book.title},
             'quantity': item.quantity}
            for item in cart_items]

    return JsonResponse(data, safe=False)


def add_to_cart(request, book_id):
    if request.method == 'POST':
        book = get_object_or_404(Book, id=book_id)
        quantity = int(request.POST.get('quantity', 1))

        cart_item, created = CartItem.objects.get_or_create(book=book)
        if cart_item.quantity is not None:
            cart_item.quantity += quantity
        else:
            cart_item.quantity = quantity
        cart_item.save()

    return redirect('index')


def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BookForm()
    return render(request, 'book_create.html', {'form': form})


def remove_from_cart(request, book_id):
    cart_item = get_object_or_404(CartItem, book_id=book_id)
    cart_item.delete()

    return redirect('index')


def index(request):
    cart = CartItem.objects.all()
    return render(request, 'index.html', {'cart': cart})
