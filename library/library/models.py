from django.db import models
import datetime
from django.utils import timezone


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    image = models.ImageField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    id = models.IntegerField(primary_key=True)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    room_number = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=60, editable=False)
    isbn = models.CharField(primary_key=True, max_length=13)
    author = models.ForeignKey(to=Author, on_delete=models.CASCADE, editable=False)
    call_number = models.CharField(max_length=10, unique=True)
    copies = models.IntegerField(default=1)
    teacher = models.ForeignKey(to=Teacher, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(blank=True)
    image = models.URLField(blank=True, null=True)
    pages = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Checkout(models.Model):
    book = models.ForeignKey(to=Book, on_delete=models.CASCADE)
    student = models.ForeignKey(to=Student, on_delete=models.CASCADE)
    checkout_time = models.DateTimeField(auto_now_add=True)
    checkin_time = models.DateTimeField(blank=True, null=True)
    due_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.student.last_name}, {self.student.first_name}; {self.book.__str__()}, Due: {self.due_date}'
