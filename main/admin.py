from django.contrib import admin
from .models import *
from django.utils.html import format_html

# Register your models here.

admin.site.register(Employee)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name","show_image"]

    def show_image(self, obj):
        return format_html('<img src="{}" width="50px" />'.format(obj.image.url))
    
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["name", "author","show_image"]

    def show_image(self, obj):
        return format_html('<img src="{}" width="50px" />'.format(obj.image.url))

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name","show_image"]

    def show_image(self, obj):
        return format_html('<img src="{}" width="50px" />'.format(obj.image.url))
