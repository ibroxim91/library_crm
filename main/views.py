from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from .models import Student, Book, Author,BookRecevier
from django.http import JsonResponse
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import StudentSerializers, BookSerializers
import datetime

# Create your views here.

class HomeView(View):
    def get(self, request):
        return render(request, 'index.html')


class StudentView(View):
    def get(self, request):
        students = Student.objects.all()
        context = {'students':students}
        return render(request, 'students.html', context=context)
    
    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        image = request.FILES.get('image')
        student_id = request.POST.get('student_id')
        print(first_name, last_name, phone, image)
        if student_id:
            student = Student.objects.get(id=int(student_id))
            student.first_name = first_name
            student.last_name = last_name
            student.phone = phone
            if image:
                student.image = image
            student.save()
            return redirect("/student")
        
        student = Student.objects.create(first_name=first_name, 
                                         last_name=last_name, phone=phone, image=image)
        return redirect("/student")
    
class StudentDeleteView(View):
    def get(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        student.delete()
        return redirect('/student')
    
class Searchstudents(APIView):
    def get(self, request):
        q = request.GET.get('q')
        if q.isdigit():
            query = Q(id=int(q))
        else:
            query = Q(first_name__icontains=q) | Q(last_name__icontains=q)
        students = Student.objects.filter(query)
        data = StudentSerializers(students, many=True)
        return Response( {"students":data.data} )

class SearchBooks(APIView):
    def get(self, request):
        q = request.GET.get('q')
        if q.isdigit():
            query = Q(id=int(q))
        else:
            query = Q(name__icontains=q) | Q(author__last_name__icontains=q) | Q(author__first_name__icontains=q)
        students = Book.objects.filter(query)
        data = BookSerializers(students, many=True)
        return Response( {"books":data.data} )
        
    
class BookView(View):
    def get(self, request):
        books = Book.objects.all()
        context = {'books':books}
        return render(request, 'books.html', context=context)
    
    def post(self, request):
        name = request.POST.get('name')
        author = request.POST.get('author')
        image = request.FILES.get('image')
        book_id = request.POST.get('book_id')
        print(name, author, image)
        if book_id:
            book = Book.objects.get(id=int(book_id))
            book.name = name
            book.author = author
            if image:
                book.image = image
            book.save()
            return redirect("/book")
        
        book = Student.objects.create(name=name, author=author, image=image)
        return redirect("/book")
    
class BookDeleteView(View):
    def get(self, request, pk):
        student = get_object_or_404(Book, pk=pk)
        student.delete()
        return redirect('/book')
    

class AuthorView(View):
    def get(self, request):
        authors = Author.objects.all()
        context = {'authors':authors}
        return render(request, 'authors.html', context=context)


class BookReciverView(View):
    def post(self, request):
        book_id = request.POST.get('book_id', None)
        student_id = request.POST.get('student_id', None)
        date = request.POST.get('date', None)
        redirect_url = request.POST.get('redirect_url', '/')
  
        book = get_object_or_404(Book , pk=int(book_id))
        student = get_object_or_404(Student , pk=int(student_id))
        end_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        bc = BookRecevier.objects.get_or_create(student=student)[0]
 
        bc.books.create(book=book,end_date=end_date)
        return redirect(redirect_url)
     