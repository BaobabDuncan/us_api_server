# -*- encoding:utf-8 -*-
'''
Created on 2011. 7. 16.

@author: bond
'''
from django.template import RequestContext, loader
from django.http import HttpResponse,HttpResponseRedirect
from common import util
from common import user
from kinggame import ct_kinggame, api, proxy


def handler_front(request):        
    aAdminUser = user.adminUser()    
    if not aAdminUser.getAdminUser():
        return HttpResponseRedirect("/login/")     
    
    t = loader.get_template('kinggame/index.html')
    c = RequestContext(request, locals())
    return HttpResponse(t.render(c))


def api_handler_sendPenalty(request):
    aSendPenalty = ct_kinggame.ct_sendPenalty(request)
    results = aSendPenalty.handleApiRequest()    
    templates = aSendPenalty.get_template()          
    c = RequestContext(request, locals())
    return HttpResponse(templates.render(c));

def api_handler_getPenalty(request):
    aGetPenalty = ct_kinggame.ct_getPenalty(request)
    results = aGetPenalty.handleApiRequest()    
    templates = aGetPenalty.get_template()          
    c = RequestContext(request, locals())
    return HttpResponse(templates.render(c));

def api_handler_choicePenalty(request):
    aChoicePenalty = ct_kinggame.ct_choicePenalty(request)
    results = aChoicePenalty.handleApiRequest()    
    templates = aChoicePenalty.get_template()          
    c = RequestContext(request, locals())
    return HttpResponse(templates.render(c));

def handler_penaltylist(request):
    aAdminUser = user.adminUser()    
    if not aAdminUser.getAdminUser():
        return HttpResponseRedirect("/login/")     
    
    penaltylist_ref = api.getPenaltyList()
    
    #print panaltylist_ref
    t = loader.get_template('kinggame/panaltylist.html')
    c = RequestContext(request, locals())
    return HttpResponse(t.render(c))

def handler_adminpenaltylist(request):
    aAdminUser = user.adminUser()    
    if not aAdminUser.getAdminUser():
        return HttpResponseRedirect("/login/")     
    
    penaltylist_ref = api.getAdminPenaltyList()
    
    t = loader.get_template('kinggame/panaltylist.html')
    c = RequestContext(request, locals())
    return HttpResponse(t.render(c))


def handler_userpenaltylist(request):
    aAdminUser = user.adminUser()    
    if not aAdminUser.getAdminUser():
        return HttpResponseRedirect("/login/")     
    
    penaltylist_ref = api.getUserPenaltyList()
    
    t = loader.get_template('kinggame/userpanaltylist.html')
    c = RequestContext(request, locals())
    return HttpResponse(t.render(c))



def handler_userpenaltydelete(request):
    aAdminUser = user.adminUser()    
    if not aAdminUser.getAdminUser():
        return HttpResponseRedirect("/login/")    
    
    penalty_id = request.REQUEST.get('id')    
    userPenaltyObject = api.getUserPenaltyById(penalty_id)
    api.deleteUserPenalty(userPenaltyObject)
    
    return HttpResponseRedirect("/kinggame/userpenaltylist/")    


def handler_userpenaltymovieadmin(request):
    aAdminUser = user.adminUser()    
    if not aAdminUser.getAdminUser():
        return HttpResponseRedirect("/login/")    
    
    penalty_id = request.REQUEST.get('id')   
    userPenaltyObject = api.getUserPenaltyById(penalty_id)
    
    penalty_para={
        'uuid':util.get_universally_unique_identifiers(),
        'detail': userPenaltyObject.detail,     
        'lang_type': userPenaltyObject.lang_type            
    }
    
    adminPanaltyVO = proxy.px_AdminPenalty().createAdminPenaltyObject(penalty_para)            
    proxy.px_AdminPenalty().insert_model_object(adminPanaltyVO)
    
    api.deleteUserPenalty(userPenaltyObject)
    
    
    return HttpResponseRedirect("/kinggame/userpenaltylist/")    
    
    
    
    