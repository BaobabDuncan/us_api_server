
from django.http import HttpResponseRedirect
from google.appengine.api import memcache

class adminUser():    
    def __init__(self):
        pass
    
    def getAdminUser(self):
        return memcache.get("adminUser")
    
    def setAdminUser(self):
        memcache.add("adminUser", "admin", 80000)