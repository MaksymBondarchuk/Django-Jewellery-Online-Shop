# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
import yagmail


@shared_task
def send_mail(name):
    yag = yagmail.SMTP('webappslab3@gmail.com', 'StrongPassword123')
    contents = ["{0} created new order".format(name)]
    yag.send('bondarchuk.m.y@gmail.com', 'New order', contents)
