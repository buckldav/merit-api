from django.db.models import fields
from rest_framework import serializers
from library.library.models import *


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    # Include all the non-editable fields here
    title = serializers.CharField(max_length=60)
    # author = serializers.PrimaryKeyRelatedField(
    #     many=False,
    #     queryset=Author.objects.all()
    # )
    last_name = serializers.CharField(source='author.last_name')
    first_name = serializers.CharField(source='author.first_name')
    pages = models.IntegerField()

    class Meta:
        model = Book
        fields = ("title", "pages", "last_name", "first_name", "call_number", "isbn", "image")


class BookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("isbn", "call_number")


class CheckoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkout
        fields = "__all__"
