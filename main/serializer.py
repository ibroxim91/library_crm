from .models import Student, Book, Author
from rest_framework import serializers

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'first_name', 'last_name')


class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name')

class BookSerializers(serializers.ModelSerializer):
    author = serializers.CharField(source='author.full_name')
    class Meta:
        model = Book
        fields = ('id', 'name', 'author')