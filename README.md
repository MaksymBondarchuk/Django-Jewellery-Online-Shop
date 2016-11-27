This message is for me from future.

After each change in models or related perform next:
> python3 manage.py makemigrations
> python3 manage.py migrate

Memcashed:

> sudo apt-get install memcached
> memcached -l 127.0.0.1 -p 12345 -m 64 -vv