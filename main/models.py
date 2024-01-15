from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core import validators

# Create your models here.

class ImageClass:
    image = models.ImageField(upload_to='images/', validators=[
        validators.FileExtensionValidator(allowed_extensions=['png','jpeg','jpg'], 
            message="Quyidagi formatdagi rasmni kiriting('png','jpeg','jpg')")
    ])

class Employee(AbstractUser):
    phone = models.CharField(max_length=13, blank=True, validators=[
        validators.MinLengthValidator(9, message="Nomerni to'liq kiriting"),
        validators.MaxLengthValidator(13, message="Nomerni to'g'ri kiriting"),
    ])

    image = models.ImageField(upload_to='images/', validators=[
        validators.FileExtensionValidator(allowed_extensions=['png','jpeg','jpg'], 
            message="Quyidagi formatdagi rasmni kiriting('png','jpeg','jpg')")
    ])

    class Meta:
        verbose_name = 'Xodim'
        verbose_name_plural = 'Xodimlar'

class Student(models.Model, ImageClass):
    first_name = models.CharField(max_length=150, blank=True, verbose_name='first_name')
    last_name = models.CharField(max_length=150, blank=True, verbose_name='last_name')
    
    phone = models.CharField(validators=[
        validators.MinLengthValidator(9,  message="Nomerni to'liq kiriting"),
        validators.MaxLengthValidator(13, message="Nomerni to'g'ri kiriting"),
    ], max_length=13, blank=True)
    image = ImageClass.image

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self) -> str:
        return self.full_name()

class Author(models.Model, ImageClass):
    first_name = models.CharField(max_length=150, blank=True, verbose_name='first_name')
    last_name = models.CharField(max_length=150, blank=True, verbose_name='last_name')
    info = models.TextField(blank=True)
    image = ImageClass.image

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

class Book(models.Model):
    name = models.CharField(max_length=150, blank=True, verbose_name='name')
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    image = ImageClass.image



class BookRecevier(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    books = models.ManyToManyField('AcceptedBooks')

    def __str__(self) -> str:
        return self.student.full_name()

class AcceptedBooks(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    end_date = models.DateTimeField()
    recived_date = models.DateTimeField(auto_now_add=True ,blank=True)
    
    def __str__(self) -> str:
        return f"{self.book.name} - {self.end_date}"
