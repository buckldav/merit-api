from django.apps import AppConfig


class LibraryConfig(AppConfig):
    name = 'library'

class DeweyDecimalConfig(AppConfig):
    name = 'dewey_decimal'

class StudentConfig(AppConfig):
    name = 'student'

class BookConfig(AppConfig):
    name = 'book'

class TeacherConfig(AppConfig):
    name = 'teacher'

class CheckoutConfig(AppConfig):
    name = 'checkout'