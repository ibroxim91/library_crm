from django.urls import path
from .views import *
app_name = 'main'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('student', StudentView.as_view(), name='students'),
    path('student/<int:pk>/delete', StudentDeleteView.as_view(), name='student_delete'),
    path('search_students', Searchstudents.as_view(), name='search_students'),
    path('search_books', SearchBooks.as_view(), name='search_books'),
    path('book', BookView.as_view(), name='books'),
    path('book/<int:pk>/delete', BookDeleteView.as_view(), name='book_delete'),
    path('author', AuthorView.as_view(), name='authors'),
]