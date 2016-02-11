# -*- coding: utf-8 -*- 
'''
Created on 2011. 7. 16.

@author: bond
'''

from common.uksmartmvcpatterns import px_ProxyParents

from pension.models import Vo_Pension_Number

class px_Number(px_ProxyParents):    
    def __init__(self):
        self.model = Vo_Pension_Number     
        px_ProxyParents.__init__(self)
        
    def createNumberValueObject(self, number_para):        
        aNumberVO = self.model(           
            uuid=number_para['uuid'],
            lotSeq=int(number_para['lotSeq']),            
            grade=number_para['grade'],
            money=number_para['money'],
            number1=number_para['number1'],
            number2=number_para['number2'],
            number3=number_para['number3'],
            number4=number_para['number4'],
            number5=number_para['number5'],
            number6=number_para['number6'],
            number7=number_para['number7']
   
        )     
        return aNumberVO
        
    def getNumber(self,lotSeq):
        try:
            query = self.model.all().filter('lotSeq =',int(lotSeq)).order('update_at')    
            results = query.fetch(100)
            return results
        except:
            return False
