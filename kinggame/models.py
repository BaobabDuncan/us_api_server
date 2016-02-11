# -*- coding: utf-8 -*- 
'''
Created on 2011. 7. 16.

@author: bond
'''

from google.appengine.ext import db

class Vo_KingGame_Admin_Penalty(db.Model):
    uuid = db.StringProperty()
    update_at = db.DateTimeProperty(auto_now_add=True)
    
    detail = db.StringProperty()
    download_count = db.IntegerProperty(default=0)
    lang_type =  db.StringProperty()
    pass_status = db.BooleanProperty(default=False)
    
    
    
class Vo_KingGame_User_Penalty(db.Model):
    uuid = db.StringProperty()
    update_at = db.DateTimeProperty(auto_now_add=True)
    
    detail = db.StringProperty()    
    lang_type =  db.StringProperty()
    move_status = db.BooleanProperty(default=False)
    