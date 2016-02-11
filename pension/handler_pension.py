# -*- encoding:utf-8 -*-
'''
Created on 2011. 7. 16.

@author: bond
'''
from django.template import RequestContext, loader
from django.http import HttpResponse,HttpResponseRedirect
import logging
from pension import ct_pension
from common import util,user
                            # To get everything
from common.BeautifulSoup import BeautifulSoup     
import re
import urllib2

import os

def handler_front(request):        
    aAdminUser = user.adminUser()    
    if not aAdminUser.getAdminUser():
        return HttpResponseRedirect("/login/")     
    
    t = loader.get_template('pension/index.html')
    c = RequestContext(request, locals())
    return HttpResponse(t.render(c))

def api_handler_getNumber(request):
    aGetNumber = ct_pension.ct_getNumber(request)
    results = aGetNumber.handleApiRequest()    
    templates = aGetNumber.get_template()          
    c = RequestContext(request, locals())
    return HttpResponse(templates.render(c));


def api_handler_saveWallPoster(request):
    aAdminUser = user.adminUser()    
    if not aAdminUser.getAdminUser():
        return HttpResponseRedirect("/login/")
    aSaveNumber = ct_pension.ct_saveNumber(request)
    results = aSaveNumber.handleApiRequest()    
    templates = aSaveNumber.get_template()          
    c = RequestContext(request, locals())
    return HttpResponse(templates.render(c));