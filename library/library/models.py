from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    image = models.ImageField(blank=True)

    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class DeweyDecimal(models.Model):
    name = models.CharField(max_length=30, unique=True)

    
    def __str__(self):
        return self.name
    
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
    title = models.CharField(max_length=60)
    barcode = models.IntegerField(primary_key=True)
    author = models.ForeignKey(to=Author, on_delete=models.CASCADE)
    dewey_decimal = models.ForeignKey(to=DeweyDecimal, on_delete=models.CASCADE)
    copies = models.IntegerField()
    teacher = models.ForeignKey(to=Teacher, on_delete=models.CASCADE, blank=True)
    description = models.TextField()
    picture = models.ImageField(blank=True)


    
    def __str__(self):
        return self.title

class Checkout(models.Model):
    book = models.ForeignKey(to=Book, on_delete=models.CASCADE)
    student = models.ForeignKey(to=Student, on_delete=models.CASCADE)
    checkout_time = models.DateTimeField()

    
    def __str__(self):
        return f"{self.student} {self.book} {self.checkout_time}"