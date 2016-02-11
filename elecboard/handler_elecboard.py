# -*- encoding:utf-8 -*-
'''
Created on May 11, 2011

@author: woosanguk
'''

from django.template import RequestContext, loader
from django.http import HttpResponse
import logging
from elecboard import ct_elecboard
from common import util

def handler_front(request):    
    t = loader.get_template('elecboard/index.html')
    c = RequestContext(request, locals())
    return HttpResponse(t.render(c))

def api_handler_sendWallPoster(request):
    aSendWall = ct_elecboard.ct_sendWall(request)
    results = aSendWall.handleApiRequest()    
    templates = aSendWall.get_template()          
    c = RequestContext(request, locals())
    return HttpResponse(templates.render(c));
 
def api_handler_getWallPoster(request):
    
    aGetWall = ct_elecboard.ct_getWall(request)
    results = aGetWall.handleApiRequest()    
    templates = aGetWall.get_template()          
    c = RequestContext(request, locals())
    return HttpResponse(templates.render(c))


    
    
    

