'''
Created on May 11, 2011

@author: woosanguk
'''
from common.uksmartmvcpatterns import ct_ControllerApi
from common import util
import logging
from smoking import proxy 

class ct_signUp(ct_ControllerApi):    
    
    def __init__(self,request):
        self.ARGUMENTS = ('username',)
        self.TEMPLATE = 'smoking/json/signup.json'
        ct_ControllerApi.__init__(self,request)    
    
    def handleApiPostRequest(self):       
        user_id = util.get_universally_unique_identifiers()   
        self.__handleInsertUser(user_id)
        self.addResultData('user_id',user_id)
    
    def __handleInsertUser(self,user_id):             
        aPx_User = proxy.px_SmokingUser()   
        user_para = self.__getUserDictionaryData(user_id)
        aUserVO = aPx_User.createUserValueObject(user_para)
        if not aPx_User.insert_model_object(aUserVO):
            raise exception.AppDbValidationError('db insert error1')
        
    def __getUserDictionaryData(self,user_id):
        user_para={
            'uuid':user_id,
            'username': self.Request.POST['username']       
        }
        return user_para
        
        
        
        