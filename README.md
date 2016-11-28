###Lab1 migrations
After each change in models or related perform next:
> python3 manage.py makemigrations

> python3 manage.py migrate

###REST
Go to and see magic
http://127.0.0.1:8000/api-auth/login

Used this manual:
http://www.django-rest-framework.org/#example


###Memcashed

> sudo apt-get install memcached

> memcached -l 127.0.0.1 -p 12345 -m 64 -vv

###Celery
Read this
https://github.com/celery/celery/tree/master/examples/django
And do as written (especially install server)

Then run worker
> celery -A Lab1 worker -l info

Yagmail manual:
> https://github.com/kootenpv/yagmail
