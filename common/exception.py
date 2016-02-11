'''
Created on Feb 18, 2011

@author: woosanguk
'''

from common import constants

class Error(Exception):
    
    pass
    '''
    def message(self):
        return "%s" % (self.__class__.__name__)
    
    def __str__(self):
        return self.message    
    '''

class AppError(Error):
    Type = None
    Extra = None
    def __init__(self,type=None,extra=None):        
        self.Type = type
        self.Extra = extra
        #self.handeleError(type)
    
    def handeleError(self):
        if self.Type==constants.APP_ERROR_TYPE['VALIDATION']:
            return self.handeleValidationError()  
        elif self.Type==constants.APP_ERROR_TYPE['DBVALIDATION']:
            return self.handeleDbValidationError()    
        elif self.Type==constants.APP_ERROR_TYPE['SYSTEM']:
            return self.handeleSystemError()             
        
    def generateErrorResponse(self,error_description):
        return error_description
    
    def createErrorDictionary(self,errorCode,errorMessage):
        error_description={
            "error_code":errorCode,
            "error_description":errorMessage,
            "error_extra":self.Extra
        }
        return error_description        
    
    def handeleValidationError(self):
        errorCode = 1001
        errorMessage = 'please input the Arguments'
        error_description = self.createErrorDictionary(errorCode,errorMessage)        
        return self.generateErrorResponse(error_description)    
    
    def handeleSystemError(self):
        errorCode = 1003
        errorMessage = 'system error'  
        error_description = self.createErrorDictionary(errorCode,errorMessage)       
        return self.generateErrorResponse(error_description)    
    
    def handeleDbValidationError(self):
        errorCode = 1002
        errorMessage = 'Do not have db information'  
        error_description = self.createErrorDictionary(errorCode,errorMessage)        
        return self.generateErrorResponse(error_description)    
    

# 1000
# 2000
# 3000
# 4000
# 5000
# 6000

class AppValidationError(Error):
    ERROR_CODE = 1001
    ERROR_MESSAGE = 'ValidationError'
    EXTRA = None
    
    def __init__(self,extra=None):
        self.EXTRA = extra
        pass
    
    def generateErrorResponse(self,error_description):
        return error_description
    def handeleError(self):
        error_description = dict(
            error_code = self.ERROR_CODE,
            error_description = self.ERROR_MESSAGE,
            error_extra = self.EXTRA
        )
        return self.generateErrorResponse(error_description)
    
class AppDbValidationError(Error):
    ERROR_CODE = 1002
    ERROR_MESSAGE = "DbValidationError"
    EXTRA = None
    
    def __init__(self,extra=None):
        self.EXTRA = extra
        pass
    
    def generateErrorResponse(self,error_description):
        return error_description
    def handeleError(self):
        error_description = dict(
            error_code = self.ERROR_CODE,
            error_description = self.ERROR_MESSAGE,
            error_extra = self.EXTRA
        )
        return self.generateErrorResponse(error_description)

class AppOauthValidationError(Error):    
    ERROR_CODE = 1004
    ERROR_MESSAGE = "OauthValidationError"
    EXTRA = None
    
    def __init__(self,extra=None):
        self.EXTRA = extra
        pass
    
    def generateErrorResponse(self,error_description):
        return error_description
    def handeleError(self):
        error_description = dict(
            error_code = self.ERROR_CODE,
            error_description = self.ERROR_MESSAGE,
            error_extra = self.EXTRA
        )
        return self.generateErrorResponse(error_description)

    
class SystemValidationError(Error):
    ERROR_CODE = 1003
    ERROR_MESSAGE = "SystemValidationError"
    EXTRA = None
    
    def __init__(self,extra=None):
        self.EXTRA = extra
        pass
    
    def generateErrorResponse(self,error_description):
        return error_description
    def handeleError(self):
        error_description = dict(
            error_code = self.ERROR_CODE,
            error_description = self.ERROR_MESSAGE,
            error_extra = self.EXTRA
        )
        return self.generateErrorResponse(error_description)
    












