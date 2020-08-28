import os

path = "C:/Users/User/Desktop/python/organize files/tmp/year"

try:
    os.makedirs(path)
except OSError:
    print ("Creation of the directory %s failed" % path)
else:
    print ("Successfully created the directory %s" % path)