# -*- encoding:utf-8 -*-
'''
Created on May 11, 2011

@author: woosanguk
'''

import logging
from common import constants,exception

from django.template import loader

class px_ProxyParents():    
    def __init__(self):
        pass
    def insert_model_object(self,valueObject):

        valueObject.save() 
        return valueObject
        
class ct_ControllerApi():
    TEMPLATE_ERROR = 'json/error.json'
    ResultsData = None
    
    def __init__(self,request):    
        self.Request = request       
        self.ResultsData = dict()
        pass
    
    def handleApiRequest(self):   
        status = False     
        try:             
            self.isArgumentsValid()                
            if (self.Request.method == constants.RequestMethod['POST']):
                self.handleApiPostRequest() 
            elif (self.Request.method == constants.RequestMethod['GET']):
                self.handleApiGetRequest()       
            else:         
                logging.info(3)     
            status = True                           
        except exception.AppValidationError, e:     
            errorResponse = e.handeleError()    
            self.addResultData('errorResponse',errorResponse)  
            
        except exception.AppDbValidationError, e:
            errorResponse = e.handeleError()    
            self.addResultData('errorResponse',errorResponse)      
        
        except exception.AppOauthValidationError, e:
            errorResponse = e.handeleError()    
            self.addResultData('errorResponse',errorResponse)                                
            
        except Exception:   
            import sys             
            error = exception.SystemValidationError(sys.exc_info()[1])
            errorResponse = error.handeleError()    
            self.addResultData('errorResponse',errorResponse)              
        
        finally:                           
            self.addResultData('status',status)   
            return self.getRequestResult()    
    # get Request Data fomat is dictionary 
    def getRequestDictionData(self):
        if self.Request.method == constants.RequestMethod['GET']: 
            thisRequest = self.Request.GET
        elif self.Request.method == constants.RequestMethod['POST']:
            thisRequest = self.Request.POST      
        else:
            raise exception.SystemValidationError('request Type wrong')
        return thisRequest
    
    def isArgumentsValid(self):
        requestData = self.getRequestDictionData()
        if (self.ARGUMENTS):
            for argument in self.ARGUMENTS: 
                if not requestData.has_key(argument):                
                    raise exception.AppValidationError("Do not have argument is %s"%(argument))
            return True 
    
    def getRequestResult(self):
        return self.ResultsData      
    
    def addResultData(self,name,data):
        self.ResultsData[name] = data
        
    def get_template(self):        
        if 'errorResponse' in self.ResultsData:              
            return loader.get_template(self.TEMPLATE_ERROR) 
        else:           
            return loader.get_template(self.TEMPLATE) 