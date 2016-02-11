'''
Created on May 11, 2011

@author: woosanguk
'''
from common.uksmartmvcpatterns import ct_ControllerApi
from common import util
import logging
from armageddon import proxy 


class ct_sendWall(ct_ControllerApi):    
    
    def __init__(self,request):
        self.ARGUMENTS = ('name','message')
        self.TEMPLATE = 'armageddon/json/sendWall.json'
        ct_ControllerApi.__init__(self,request)    
    
    def handleApiPostRequest(self):       
        self.__handleInsertWall()        
    
    def __handleInsertWall(self):             
        aPx_Wall = proxy.px_WallPoster()
        
        wall_para = self.__getWallDictionaryData()
        aWallVO = aPx_Wall.createWallValueObject(wall_para)
        
        if not aPx_Wall.insert_model_object(aWallVO):
            raise exception.AppDbValidationError('db insert error1')
        
    def __getWallDictionaryData(self):
        wall_para={
            'uuid':util.get_universally_unique_identifiers(),
            'name': self.Request.POST['name'],
            'message': self.Request.POST['message']      
        }
        return wall_para
    
class ct_getWall(ct_ControllerApi):
    
    def __init__(self,request):
        self.ARGUMENTS = False
        self.TEMPLATE = 'armageddon/json/getWall.json'
        ct_ControllerApi.__init__(self,request)    
        
    def handleApiGetRequest(self):
        self.__handleSelectWall()
       
    def __handleSelectWall(self):
        aPx_Wall = proxy.px_WallPoster()        
        wall_ref = aPx_Wall.getWallPoster()
        self.addResultData('wall_ref',wall_ref)
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    