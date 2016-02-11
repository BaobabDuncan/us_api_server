# -*- encoding:utf-8 -*-
'''
Created on May 11, 2011

@author: woosanguk
'''

from django.template import RequestContext, loader
from django.http import HttpResponse
from common import constants, util

import logging
import os
from sixstreet import proxy_sixstreet

def handler_front(request):    
    t = loader.get_template('sixstreet/index.html')
    c = RequestContext(request, locals())
    return HttpResponse(t.render(c));


def handler_createClub(request):
    if request.method == constants.RequestMethod['POST']:
        aPx_Club = proxy_sixstreet.px_Club()
        club_para = {
            'uuid':util.get_universally_unique_identifiers(),
            'name': request.POST['name'],
            'detail': request.POST['detail']      
        }

        #print '한구'

        print test
        #print request.POST['name'].encode('ascii')
        #print u'%s'%request.POST['name']
        #print unicode(request.POST['name'],'utf8')
        #aClubVO = aPx_Club.createClubValueObject(club_para)
        #aPx_Club.insert_model_object(aClubVO)
    if request.method == constants.RequestMethod['GET']:
        print request.GET['name']
    t = loader.get_template('sixstreet/index.html')
    c = RequestContext(request, locals())
    return HttpResponse(t.render(c));


def handler_createMember(request):    
    if request.method == constants.RequestMethod['POST']:
        aPx_Club = proxy_sixstreet.px_Club()
        aPx_Member = proxy_sixstreet.px_Member()
        club_ref = aPx_Club.getClubByClubId(request.POST['club_id'])
        
        
        fileUrl = "site_files/sixstreet/%s/list.txt"%(request.POST['club_id'])
        
        filePath = os.path.join(fileUrl)
        file = open(filePath,'r')     
        logging.info(file)
        
        for member in file.read().split('\n'):
            member_list = member.split('|')            
            mamber_para = {
                'uuid' : util.get_universally_unique_identifiers(),
                'member_id' : member_list[0].strip(),
                'club_id' : request.POST['club_id'],                
                'name' : member_list[1].strip(),
                'nick' : member_list[6].strip(),
                'tel' : member_list[2].strip(),
                'address' : member_list[3].strip(),
                'mail' : member_list[4].strip(),
                'birth' : member_list[5].strip()          
            }           
            logging.info(mamber_para)
            #aMemberVO = aPx_Member.createMemberValueObject(mamber_para)
            
            #aPx_Member.insert_model_object(aMemberVO)
            #for member_value in member.split('|'):                
                #print member_value.strip()
            
        #for word in file.read().split('^'): 
            #logging.info(word)
        
        
        
        
    t = loader.get_template('sixstreet/index.html')
    c = RequestContext(request, locals())
    return HttpResponse(t.render(c));
    
    
    
def api_handler_getClubList(request):
    aSendWall = ct_armageddon.ct_sendWall(request)
    results = aSendWall.handleApiRequest()    
    templates = aSendWall.get_template()          
    c = RequestContext(request, locals())
    return HttpResponse(templates.render(c));
    
def api_handler_getClubMember(request):
    aGetWall = ct_armageddon.ct_getWall(request)
    results = aGetWall.handleApiRequest()    
    templates = aGetWall.get_template()          
    c = RequestContext(request, locals())
    return HttpResponse(templates.render(c));


    
    
    

