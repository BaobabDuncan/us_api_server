# -*- encoding:utf-8 -*-
'''
Created on May 11, 2011

@author: woosanguk
'''
from common.uksmartmvcpatterns import px_ProxyParents

from elecboard.models import Vo_Elec_WallPoster

class px_WallPoster(px_ProxyParents):    
    def __init__(self):
        self.model = Vo_Elec_WallPoster     
        px_ProxyParents.__init__(self)
        
    def createWallValueObject(self,wall_para):        
        aWallVO = self.model(
            uuid = wall_para['uuid'],
            name = wall_para['name'],
            message = wall_para['message']           
        )     
        return aWallVO
    
    def getWallPoster(self):
        query = self.model.all().order('-update_at')
        results = query.fetch(100)
        return results