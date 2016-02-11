# -*- encoding:utf-8 -*-
'''
Created on May 11, 2011

@author: woosanguk
'''
from common.uksmartmvcpatterns import ct_ControllerApi
from common import util,exception
import logging
from armageddon import proxy 


class ct_sendWall(ct_ControllerApi):    
    
    def __init__(self,request):       
        self.ARGUMENTS = ('name','message')
        self.TEMPLATE = 'armageddon/json/sendWall.json'
        ct_ControllerApi.__init__(self,request)    
    
    def handleApiGetRequest(self):       
        self.__handleInsertWall()      
        self.addResultData('callback',self.Request.REQUEST.get('callback',''))     
    
    def handleApiPostRequest(self):       
        self.__handleInsertWall()        
        self.addResultData('callback',self.Request.REQUEST.get('callback',''))     
    
    def __handleInsertWall(self):             
        aPx_Wall = proxy.px_WallPoster()
        
        wall_para = self.__getWallDictionaryData()
        aWallVO = aPx_Wall.createWallValueObject(wall_para)
        
        if not aPx_Wall.insert_model_object(aWallVO):
            raise exception.AppDbValidationError('db insert error1')
        
        
    def __getWallDictionaryData(self):
        logging.info('123123')
        
        logging.info(self.Request.REQUEST.get('update_at').decode('utf8'))    
        wall_para={
            'uuid':util.get_universally_unique_identifiers(),
            'name': self.Request.REQUEST.get('name').decode('utf8'),
            'message': self.Request.REQUEST.get('message').decode('utf8'),
            'update_at' :self.Request.REQUEST.get('update_at').decode('utf8')   
        }
        return wall_para
    
class ct_getWall(ct_ControllerApi):
    
    def __init__(self,request):
        self.ARGUMENTS = False
        self.TEMPLATE = 'armageddon/json/getWall.json'
        ct_ControllerApi.__init__(self,request)    
        
    def handleApiGetRequest(self):
       
        self.__handleSelectWall()              
        self.addResultData('callback',self.Request.REQUEST.get('callback',''))       
        
        
    def __handleSelectWall(self):        
        aPx_Wall = proxy.px_WallPoster()        
        wall_ref = aPx_Wall.getWallPoster(self.Request.REQUEST.get('next'))
        self.addResultData('wall_ref',wall_ref)
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    