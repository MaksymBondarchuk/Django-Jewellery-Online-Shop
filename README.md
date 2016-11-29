###Mongo
Setting up MongoDB:
1. Create config file mongod.cfg like
"bind_ip = 127.0.0.1
dbpath = C:\mongodb\data\db
logpath = C:\mongodb\log\mongo-server.log
verbose=v"
2. > mongod --config mongod.cfg --install

3. > net start MongoDB

4. run mongo (optional)


To setup Django MongoDB:
1. > pip install git+https://github.com/django-nonrel/django@nonrel-1.5
2. > pip install git+https://github.com/django-nonrel/djangotoolbox
3. > pip install git+https://github.com/django-nonrel/mongodb-engine