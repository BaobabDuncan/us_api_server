'''
Created on 2012. 2. 4.

@author: bond
'''
from common.uksmartmvcpatterns import ct_ControllerApi
from common import util,exception
from kinggame import proxy, api
import logging

class ct_choicePenalty(ct_ControllerApi):
    
    def __init__(self,request):       
        self.ARGUMENTS = ('penalty_id',)
        self.TEMPLATE = 'kinggame/json/choicePenalty.json'        
        ct_ControllerApi.__init__(self,request)  
        
    def handleApiPostRequest(self):        
        
        penaltyObject = api.getAdminPenaltyById(self.Request.REQUEST.get('penalty_id'))
        api.updateDownloadCount(penaltyObject)
        
class ct_getPenalty(ct_ControllerApi):
    
    def __init__(self,request):       
        self.ARGUMENTS = False
        self.TEMPLATE = 'kinggame/json/getPenalty.json'        
        ct_ControllerApi.__init__(self,request)  
        
    def handleApiGetRequest(self):         
        
        penaltylist_ref = api.getTopPenaltyList(self.Request.REQUEST.get('type'),self.Request.REQUEST.get('next'))       
        
        penaltylist_ref = penaltylist_ref
        self.addResultData('penalty_ref',penaltylist_ref)
        
        
class ct_sendPenalty(ct_ControllerApi):
    
    def __init__(self,request):       
        self.ARGUMENTS = ('detail','lang_type','type')
        self.TEMPLATE = 'kinggame/json/sendPanalty.json'
        ct_ControllerApi.__init__(self,request)  
    
    def __getPenaltyDictionaryData(self):
        panalty_para={
            'uuid':util.get_universally_unique_identifiers(),
            'detail': self.Request.REQUEST.get('detail').decode('utf8'),     
            'lang_type': self.Request.REQUEST.get('lang_type').decode('utf8')                   
        }
        return panalty_para     
        
    def __handleInsertPenalty(self):           
        insertType = self.Request.REQUEST.get('type','')  
              
        penalty_para = self.__getPenaltyDictionaryData()
        
        if (insertType=='user'):            
            userPanaltyVO = proxy.px_UserPenalty().createUserPenaltyObject(penalty_para)            
            if not proxy.px_UserPenalty().insert_model_object(userPanaltyVO):
                raise exception.AppDbValidationError('db insert error')
        elif (insertType=='admin'):
            adminPanaltyVO = proxy.px_AdminPenalty().createAdminPenaltyObject(penalty_para)            
            if not proxy.px_AdminPenalty().insert_model_object(adminPanaltyVO):
                raise exception.AppDbValidationError('db insert error')
        else:
            raise exception.AppValidationError('null allow this type')
        
        
    def handleApiPostRequest(self):    
        '''
            check type
                1. insert panalty
        '''         
        self.__handleInsertPenalty()
        #self.__checkSendType()
        
        
        
        
        #self.__handleInsertWall()        
        