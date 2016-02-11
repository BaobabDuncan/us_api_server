'''
Created on May 11, 2011

@author: woosanguk
'''

from google.appengine.ext import db

class Vo_SmokingUser(db.Model):
    uuid = db.StringProperty()
    update_at = db.DateTimeProperty(auto_now_add=True)
    username = db.StringProperty()
    money = db.FloatProperty(default=0.0)
    quit_count = db.IntegerProperty(default=0)





    

    