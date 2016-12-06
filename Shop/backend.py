import yagmail
from celery import Celery

app = Celery('hello', broker='amqp://guest@localhost//')


@app.task
def send_mail(name):
    yag = yagmail.SMTP('webappslab3@gmail.com', 'StrongPassword123')
    contents = ["%s created new order" % name]
    yag.send('bondarchuk.m.y@gmail.com', 'New order', contents)
