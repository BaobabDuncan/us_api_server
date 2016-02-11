# -*- encoding:utf-8 -*-
'''
Created on May 11, 2011

@author: woosanguk
'''
from common.uksmartmvcpatterns import px_ProxyParents

from kinggame.models import Vo_KingGame_Admin_Penalty,Vo_KingGame_User_Penalty

PAGESIZE = 20


class px_UserPenalty(px_ProxyParents):
    def __init__(self):
        self.model = Vo_KingGame_User_Penalty     
        px_ProxyParents.__init__(self)
    
    def createUserPenaltyObject(self,panalty_para):
        aUserPenaltyVO = self.model(
            uuid = panalty_para['uuid'],
            detail = panalty_para['detail'],
            lang_type = panalty_para['lang_type'],                   
        )     
        return aUserPenaltyVO
    
    def getUserPenaltyList(self):
        query = self.model.all().filter('move_status =', False).order('-update_at')
        
        return query
    
    def getUserPenaltyById(self,aId):
        query = self.model.all().filter('uuid =', aId).get()
        return query

class px_AdminPenalty(px_ProxyParents):
    def __init__(self):
        self.model = Vo_KingGame_Admin_Penalty     
        px_ProxyParents.__init__(self)
        
    def getAdminPenaltyById(self,aId):
        query = self.model.all().filter('uuid =', aId).get()
        return query
        
    def createAdminPenaltyObject(self,panalty_para):
        aAdminPenaltyVO = self.model(
            uuid = panalty_para['uuid'],
            detail = panalty_para['detail'],
            lang_type = panalty_para['lang_type'],                   
        )     
        return aAdminPenaltyVO
    
    def getPenaltyList(self):
        query = self.model.all().filter('pass_status =', True).order('-update_at')
        
        return query
    
    def getTopPenaltyList(self,type,next):
        if(next):        
            oPenalty =  self.model.all().filter('uuid =', next).get()                       
            query = self.model.all().filter('update_at <', oPenalty.update_at).filter('pass_status =', False).filter('lang_type =', type).order('-update_at')   
            #query = self.model.all().order('-update_at').filter('pass_status =', False).filter('update_at <', oPenalty.update_at)            
        else:            
            query = self.model.all().filter('pass_status =', False).filter('lang_type =', type).order('-update_at')
        results = query.fetch(PAGESIZE)   
        return results

    def getAdminPenaltyList(self,next=None):
        if(next):                   
            oPenalty =  self.model.all().filter('uuid =', next).get()                       
            query = self.model.all().order('-update_at').filter('update_at <', oPenalty.update_at).filter('pass_status =', False)     
            #query = self.model.all().order('-update_at').filter('pass_status =', False).filter('update_at <', oPenalty.update_at)            
        else:            
            query = self.model.all().filter('pass_status =', False).order('-update_at')
        results = query.fetch(PAGESIZE)       
        
        #query = self.model.all().filter('pass_status =', False).order('-update_at')
        
        return results

    


'''
class px_WallPoster(px_ProxyParents):    
    def __init__(self):
        self.model = Vo_WallPoster     
        px_ProxyParents.__init__(self)
        
    def createWallValueObject(self,wall_para):        
        aWallVO = self.model(
            uuid = wall_para['uuid'],
            name = wall_para['name'],
            message = wall_para['message'],
            #update_at = wall_para['update_at']             
        )     
        return aWallVO
    
    def getWallPoster(self,next=None):        
        if(next):                        
            oWall =  self.model.all().filter('uuid =', next).get()                 
            query = self.model.all().order('-update_at').filter('update_at <', oWall.update_at)            
        else:            
            query = self.model.all().order('-update_at')
        results = query.fetch(PAGESIZE)       
        return results
'''