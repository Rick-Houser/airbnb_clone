import os

name = os.environ.get('AIRBNB_ENV')
print name

if name == "production":
    PORT = 3000
    errorlog = '/var/log/airbnb_api/error.log'
    accesslog = '/var/log/airbnb_api/access.log'
    print "running production"

elif name == "test":
    PORT = 5555
    errolog = '-'
    accesslog = '-'
    print "running test"


elif name == "development":
    PORT = 3333
    errolog = '-'
    accesslog = '-'
    print "running development"

bind = "0.0.0.0:" + str(PORT)
reload = True
