from django.urls import path, include

from drf_yasg.views import get_schema_view
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from rest_framework import generics, permissions, status
from rest_framework.response import Response

from .serializers import *
from library.library.tasks import send_overdue_email
from library.library.models import *
import requests
import json
from stdnum.isbn import to_isbn10


class AuthorView(generics.ListCreateAPIView):
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Author.objects.all()


class AuthorDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Author.objects.all()


class StudentView(generics.ListCreateAPIView):
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Student.objects.all()
        first_name = self.request.query_params.get('first_name')
        last_name = self.request.query_params.get('last_name')
        idnum = self.request.query_params.get('id')
        email = self.request.query_params.get('email')
        if first_name is not None:
            queryset = queryset.filter(first_name__icontains=first_name)
        if last_name is not None:
            queryset = queryset.filter(last_name__icontains=last_name)
        if idnum is not None:
            queryset = queryset.filter(id__iexact=idnum)
        if email is not None:
            queryset = queryset.filter(email__icontains=email)
        return queryset


class StudentDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Student.objects.all()


class TeacherView(generics.ListCreateAPIView):
    serializer_class = TeacherSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Teacher.objects.all()
        first_name = self.request.query_params.get('first_name')
        last_name = self.request.query_params.get('last_name')
        email = self.request.query_params.get('email')
        room_number = self.request.query_params.get('room_number')
        if first_name is not None:
            queryset = queryset.filter(first_name__icontains=first_name)
        if last_name is not None:
            queryset = queryset.filter(last_name__icontains=last_name)
        if email is not None:
            queryset = queryset.filter(email__icontains=email)
        if room_number is not None:
            queryset = queryset.filter(room_number__iexact=room_number)
        return queryset


class TeacherDetailView(generics.RetrieveAPIView):
    serializer_class = TeacherSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Teacher.objects.all()


class BookView(generics.ListCreateAPIView):
    serializer_class = BookCreateSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Book.objects.all()
        title = self.request.query_params.get('title')
        author = self.request.query_params.get('author')
        barcode = self.request.query_params.get('barcode')
        call_number = self.request.query_params.get('call_number')
        if title is not None:
            queryset = queryset.filter(title__icontains=title)
        if author is not None:
            queryset = queryset.filter(author__id=int(author))
        if barcode is not None:
            queryset = queryset.filter(barcode__iexact=barcode)
        if call_number is not None:
            queryset = queryset.filter(call_number__id=int(call_number))
        return queryset

    def list(self, request):
        queryset = self.get_queryset()
        serializer = BookReadSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        """The openlibrary likes ISBN 10s"""

        ISBN = request.data["isbn"]  # "0765326353"
        if len(ISBN) == 13:
            ISBN = ISBN[0:3] + "-" + ISBN[3:]
            ISBN = to_isbn10(ISBN).strip("-")

        URL = f"https://openlibrary.org/api/books.json?jscmd=data&bibkeys=ISBN:{ISBN}"
        page = requests.get(URL)
        data = json.loads(page.content.decode("utf-8"))

        obj = {}
        obj["title"] = data[f"ISBN:{ISBN}"]["title"].title()
        if "cover" in data[f"ISBN:{ISBN}"]:
            obj["image"] = data[f"ISBN:{ISBN}"]["cover"]["medium"]
        if "number_of_pages" in data[f"ISBN:{ISBN}"]:
            obj["pages"] = int(data[f"ISBN:{ISBN}"]["number_of_pages"])
        obj["isbn"] = ISBN
        obj["call_number"] = request.data["call_number"]

        first_name = ""
        last_name = ""
        if "first_name" in request.data and request.data["first_name"] and "last_name" in request.data and request.data["last_name"]:
            first_name = request.data["first_name"]
            last_name = request.data["last_name"]
        else:
            first_name = " ".join(data[f"ISBN:{ISBN}"]["authors"][0]["name"].split()[0:-1])
            last_name = data[f"ISBN:{ISBN}"]["authors"][0]["name"].split()[-1]
        author = Author.objects.get_or_create(
            first_name=first_name,
            last_name=last_name
        )

        obj["author"] = author[0].id
        print(obj)
        serializer = BookSerializer(data=obj)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookReadSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Book.objects.all()


class CheckoutView(generics.ListCreateAPIView):
    serializer_class = CheckoutReadSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Checkout.objects.all()
        if self.request.method == "GET":
            queryset = queryset.filter(checkin_time__isnull=True)
        book = self.request.query_params.get('book')
        student = self.request.query_params.get('student')
        if book is not None:
            queryset = queryset.filter(book__title__icontains=book)
        if student is not None:
            queryset = queryset.filter(student__id=int(student))
        return queryset

    def create(self, request):
        serializer = CheckoutSerializer(data=request.data)
        if serializer.is_valid():
            checkout = serializer.save()
            checkout.due_date = datetime.datetime.now() + datetime.timedelta(days=21)
            checkout.save()
            # send_overdue_email(checkout)
        else:
            pass
            # import pdb
            # pdb.set_trace()

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class CheckoutDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CheckoutSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Checkout.objects.all()


library_schema_view = get_schema_view(
    openapi.Info(
        title="Library API",
        default_version='v1',
        description="Merit Academy Library API",
        contact=openapi.Contact(email="david.buckley@meritacademy.org"),
        license=openapi.License(name="BSD License"),
    ),
    patterns=[
        path("api/library/", include("library.library.api.urls"))
    ],
    public=False,
    permission_classes=(permissions.IsAuthenticated,),
)
