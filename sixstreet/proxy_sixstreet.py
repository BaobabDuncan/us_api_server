# -*- coding: utf-8 -*-
'''
Created on May 11, 2011

@author: woosanguk
'''
from common.uksmartmvcpatterns import px_ProxyParents

from sixstreet.models import Vo_Club,Vo_Member

class px_Club(px_ProxyParents):    
    def __init__(self):
        self.model = Vo_Club     
        px_ProxyParents.__init__(self)
        
    def createClubValueObject(self,club_para):        
        Vo_Club = self.model(
            club_id = club_para['uuid'],            
            name = club_para['name'],
            detail = club_para['detail']            
        )     
        return Vo_Club
    def getClubByClubId(self,club_id):
        query = self.model.gql('WHERE club_id = :1',club_id)
        return query.get()
        
        
class px_Member(px_ProxyParents):    
    def __init__(self):
        self.model = Vo_Member     
        px_ProxyParents.__init__(self)
        
    def createMemberValueObject(self,member_para):
        Vo_Member = self.model(
            member_id = member_para['member_id'],         
            club_id = member_para['club_id'],                        
            name = member_para['name'],         
            nick = member_para['nick'],         
            tel = member_para['tel'],         
            address = member_para['address'],         
            mail = member_para['mail'],         
            birth = member_para['birth'],   
        )     
        return Vo_Member