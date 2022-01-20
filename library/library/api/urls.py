from django.urls import path
from .views import AuthorView, StudentView, StudentDetailView, TeacherView, TeacherDetailView, BookView, BookDetailView, CheckoutView, CheckoutDetailView

urlpatterns = [
    path("authors/", AuthorView.as_view(), name="authors"),
    path("students/", StudentView.as_view(), name="students"),
    path("students/<int:pk>", StudentDetailView.as_view(), name="student-detail"),
    path("teachers/", TeacherView.as_view(), name="teachers"),
    path("teachers/<int:pk>", TeacherDetailView.as_view(), name="teacher-detail"),
    path("books/", BookView.as_view(), name="books"),
    path("books/<str:pk>", BookDetailView.as_view(), name="book-detail"),
    path("checkouts/", CheckoutView.as_view(), name="checkouts"),
    path("checkouts/<int:pk>", CheckoutDetailView.as_view(), name="checkout-detail"),
]
