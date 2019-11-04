from rest_framework import viewsets
from .models import User, Order, Book
from .serializers import UserSerializer, OrderSerializer, BookSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


from django.shortcuts import render

def indexView(request):
    return render(request, 'index.html')
