# -*- coding: utf-8 -*- 
'''
Created on 2011. 7. 16.

@author: bond
'''

from google.appengine.ext import db

class Vo_Pension_Number(db.Model):
    uuid = db.StringProperty()
    lotSeq = db.IntegerProperty()
    update_at = db.DateTimeProperty(auto_now_add=True)
    grade = db.StringProperty()
    money = db.StringProperty()
    number1 = db.StringProperty()
    number2 = db.StringProperty()
    number3 = db.StringProperty()
    number4 = db.StringProperty()
    number5 = db.StringProperty()
    number6 = db.StringProperty()
    number7 = db.StringProperty()
