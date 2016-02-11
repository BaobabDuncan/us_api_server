# -*- encoding:utf-8 -*-
'''
Created on May 11, 2011

@author: woosanguk
'''

from google.appengine.ext import db

class Vo_WallPoster(db.Model):
    uuid = db.StringProperty()
    update_at = db.DateTimeProperty(auto_now_add=True)
    name = db.StringProperty()
    message = db.StringProperty()
    






    

    