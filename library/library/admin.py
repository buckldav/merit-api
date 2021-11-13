from django.contrib import admin
from library.library.models import Author, Book, Checkout, DeweyDecimal, Student, Teacher

# Register your models here.
 
admin.site.register(Author)
admin.site.register(DeweyDecimal)
admin.site.register(Student)
admin.site.register(Book)
admin.site.register(Teacher)
admin.site.register(Checkout)