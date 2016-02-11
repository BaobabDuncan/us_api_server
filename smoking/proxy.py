'''
Created on May 11, 2011

@author: woosanguk
'''
from common.uksmartmvcpatterns import px_ProxyParents

from smoking.models import Vo_SmokingUser

class px_SmokingUser(px_ProxyParents):    
    def __init__(self):
        self.model = Vo_SmokingUser     
        px_ProxyParents.__init__(self)
        
    def createUserValueObject(self,user_para):        
        aUserVO = self.model(
            uuid = user_para['uuid'], 
            username = user_para['username']                 
        )     
        return aUserVO   
       