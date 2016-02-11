# -*- coding: utf-8 -*-
'''
Created on May 11, 2011

@author: woosanguk
'''

from google.appengine.ext import db

class Vo_Club(db.Model):
    club_id = db.StringProperty()
    update_at = db.DateTimeProperty(auto_now_add=True)
    name = db.StringProperty()
    detail = db.StringProperty()
    total_member = db.IntegerProperty(default=0)
    
class Vo_Member(db.Model):
    uuid = db.StringProperty()
    member_id = db.StringProperty()
    club_id = db.StringProperty()
    update_at = db.DateTimeProperty(auto_now_add=True)
    name = db.StringProperty()
    nick = db.StringProperty()
    tel = db.StringProperty()
    address = db.StringProperty()
    mail = db.StringProperty()
    birth = db.StringProperty()
    






    

    