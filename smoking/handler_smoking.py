'''
Created on May 11, 2011

@author: woosanguk
'''

from django.template import RequestContext, loader
from django.http import HttpResponse,HttpResponseRedirect
import logging
from smoking import ct_smoking
from common import user

def handler_front(request):    
    aAdminUser = user.adminUser()    
    if not aAdminUser.getAdminUser():
        return HttpResponseRedirect("/login/")     
    t = loader.get_template('smoking/index.html')
    c = RequestContext(request, locals())
    return HttpResponse(t.render(c));

def api_handler_signUp(request):      
    aAdminUser = user.adminUser()    
    if not aAdminUser.getAdminUser():
        return HttpResponseRedirect("/login/")         
    aSignUp = ct_smoking.ct_signUp(request)
    results = aSignUp.handleApiRequest()    
    templates = aSignUp.get_template()          
    c = RequestContext(request, locals())
    return HttpResponse(templates.render(c));

def api_handler_sendMoney(request):    
    aAdminUser = user.adminUser()    
    if not aAdminUser.getAdminUser():
        return HttpResponseRedirect("/login/")     
    t = loader.get_template('smoking/index.html')
    c = RequestContext(request, locals())
    return HttpResponse(t.render(c));

def api_handler_getTopRanking(request):    
    aAdminUser = user.adminUser()    
    if not aAdminUser.getAdminUser():
        return HttpResponseRedirect("/login/")     
    t = loader.get_template('smoking/index.html')
    c = RequestContext(request, locals())
    return HttpResponse(t.render(c));

def api_handler_resetMoney(request):    
    aAdminUser = user.adminUser()    
    if not aAdminUser.getAdminUser():
        return HttpResponseRedirect("/login/")     
    t = loader.get_template('smoking/index.html')
    c = RequestContext(request, locals())
    return HttpResponse(t.render(c));

