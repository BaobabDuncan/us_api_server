# -*- coding: utf-8 -*- 
'''
Created on 2011. 7. 16.

@author: bond
'''
from common.uksmartmvcpatterns import ct_ControllerApi
from google.appengine.api import memcache
from common import util, exception
import logging
from pension import proxy 

from common.BeautifulSoup import BeautifulSoup     
import re
import urllib2
import sys

class ct_saveNumber(ct_ControllerApi):
    def __init__(self,request):
        self.ARGUMENTS = ('lotSeq','grade')
        self.TEMPLATE = 'armageddon/json/sendWall.json'
        ct_ControllerApi.__init__(self,request)  
          
    def handleApiPostRequest(self):       
        #self.__handleInsertWall()        
        aPx_Number = proxy.px_Number()   
        wall_para={
            'uuid':util.get_universally_unique_identifiers(),
            'lotSeq': self.Request.REQUEST.get('lotSeq'),
            'grade': self.Request.REQUEST.get('grade').decode('utf8'),
            'money': self.Request.REQUEST.get('money').decode('utf8'),
            'number1': self.Request.REQUEST.get('number1').decode('utf8'),
            'number2': self.Request.REQUEST.get('number2'),
            'number3': self.Request.REQUEST.get('number3'),
            'number4': self.Request.REQUEST.get('number4'),
            'number5': self.Request.REQUEST.get('number5'),
            'number6': self.Request.REQUEST.get('number6'),
            'number7': self.Request.REQUEST.get('number7')       
        }      
        
        aNumberVO = aPx_Number.createNumberValueObject(wall_para)            
        aPx_Number.insert_model_object(aNumberVO)       
        self.addResultData('callback',self.Request.REQUEST.get('callback',''))     
        
class ct_getNumber(ct_ControllerApi):    
    
    GRADE = ('1등', '1등', '2등', '2등', '2등', '2등', '3등', '4등', '5등', '6등', '6등', '7등', '7등')
    MONEY = ('매달500만원x20년', '매달500만원x20년', '100,000,000', '100,000,000', '100,000,000', '100,000,000', '10,000,000', '1,000,000', '200,000', '2,000', '2,000', '1,000', '1,000')
    
    def __init__(self, request):
        self.ARGUMENTS = ('lotSeq',)
        self.TEMPLATE = 'pension/json/getNumber.json'
        ct_ControllerApi.__init__(self, request)    
        
    def handleApiGetRequest(self):       
        self.__handleGetNumber()      
        self.addResultData('callback', self.Request.REQUEST.get('callback', ''))   
    
    def __handleGetNumber(self):             
        aPx_Number = proxy.px_Number()   
        lotSeq = int(self.Request.REQUEST.get('lotSeq'))
        
        numberCacheKey = self.__getNumberCacheKey(lotSeq)               
        Number_ref = memcache.get(numberCacheKey)
        #Number_ref = None
        if not Number_ref:                   
            Number_ref = aPx_Number.getNumber(lotSeq)
            #self.__getNumberFromHomePage(self.Request.REQUEST.get('lotSeq'))            
            if not Number_ref:                         
                saveData = self.__getNumberFromHomePage(lotSeq)  
                if not saveData:
                    raise exception.AppDbValidationError('data false')
                else:               
                    Number_ref = aPx_Number.getNumber(lotSeq)                
            memcache.add(numberCacheKey, Number_ref)     
        
        self.addResultData('Number_ref', Number_ref)
                
    def __getNumberCacheKey(self,lotSeq):          
        return "pension_%s"%(lotSeq)
       
    def __getNumberFromHomePage(self, aLotSeq):        
        aPx_Number = proxy.px_Number()        
        opener = urllib2.build_opener()
        flood = False
        try:
            contents = opener.open('http://www.bokgwon.or.kr/annuity520_lotteryNo.do').read()
                
        except:            
            contents = opener.open('http://www.bokgwon.or.kr/').read()
            flood = True
        
        soup_contents = BeautifulSoup(contents)
        
        if flood:           
            info = soup_contents.find('td', {"class":"numtitle"})               
            lotSeq = info.next.strip()[2:3]                
        else:            
            info = soup_contents.find('div', {"class":"t_floatL"})        
            lotSeq = info.find('span').next                
        
        if int(aLotSeq) != int(lotSeq):                           
            return False        
        contents_tr = soup_contents.findAll('tr')        
        index = 0
        
        for tr in contents_tr:
            #print self.GRADE[count]
            para = {            
            }
            if not (tr.find('th', {"class":"title021"})):
                continue
            
            
            count = 0
            for title in tr.findAll('th', {"class":"title021"}):                   
                if count == 0:
                    count = count + 1
                    continue            
                
                elif count == 1:
                    if index < 6:
                        para['number1'] = title.next.strip()[:1] + u'조'      
                        #para['number1'] = title.next.strip()
                    else:
                        para['number1'] = u'각조'
                elif count == 2:
                    if index < 7:
                        para['number2'] = title.next.strip()
                    else:
                        para['number2'] = u'-'
                elif count == 3:
                    if index < 8:
                        para['number3'] = title.next.strip()
                    else:
                        para['number3'] = u'-'
                elif count == 4:
                    if index < 9:
                        para['number4'] = title.next.strip()
                    else:
                        para['number4'] = u'-'
                elif count == 5:
                    if index < 9:
                        para['number5'] = title.next.strip()
                    else:
                        para['number5'] = u'-'                   
                elif count == 6:
                    if index < 11:
                        para['number6'] = title.next.strip()
                    else:
                        para['number6'] = u'-'   
                
                count = count + 1
            
            para['number7'] = tr.find('th', {"class":"title031"}).next.strip()  
            para['money'] = self.MONEY[index].decode("utf-8")
            para['uuid'] = util.get_universally_unique_identifiers()
            para['lotSeq'] = lotSeq.strip()      
            para['grade'] = self.GRADE[index].decode("utf-8")
                         
            aNumberVO = aPx_Number.createNumberValueObject(para)            
            aPx_Number.insert_model_object(aNumberVO)
            index = index + 1
        return True
#        
