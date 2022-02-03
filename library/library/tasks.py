from django.conf import settings
from django.core.mail import send_mail
from library.library.models import Checkout
# from celery import shared_task
from celery.contrib.abortable import AbortableTask
from config.settings.celery import app
from time import sleep


@app.task(bind=True, base=AbortableTask)
def send_overdue_email(self, checkout):
    sleep((checkout.due_date - checkout.checkout_time).total_seconds())
    # try to get checkout object from db if exists
    try:
        # print("email!")
        checkout = Checkout.objects.get(id=checkout.id)
        recipient = checkout.student.email  # recipient = student email
        send_mail('Book overdue at Merit Library', f'{checkout.book.title} is overdue. Please turn it in.', settings.EMAIL_HOST_USER, [
                  recipient], fail_silently=False)
    except:
        # the book was checked in
        pass
