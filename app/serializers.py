from rest_framework import serializers
from .models import User, Order, Book

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    # book = serializers.StringRelatedField(many=True)
    class Meta:
        model = Order
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
