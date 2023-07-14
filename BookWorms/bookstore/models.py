from django import forms
from django.db import models
from decimal import Decimal


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()


class CartItem(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    @property
    def total_cost(item):
        item_quantity = item.quantity
        item_price = item.book.price.to_decimal()
        total_price = Decimal(item_quantity) * item_price
        return total_price


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'price', 'description']
