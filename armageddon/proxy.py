# -*- encoding:utf-8 -*-
'''
Created on May 11, 2011

@author: woosanguk
'''
from common.uksmartmvcpatterns import px_ProxyParents

from armageddon.models import Vo_WallPoster
PAGESIZE = 20
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