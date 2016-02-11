# -*- encoding:utf-8 -*-
'''
Created on May 11, 2011

@author: woosanguk
'''

from django.template import RequestContext, loader
from django.http import HttpResponse
import logging
from armageddon import ct_armageddon
from common import util
import datetime
def handler_front(request):    
    logging.info('handler_front')
    logging.info(datetime.datetime(1985,12,26,8,8,8))
    t = loader.get_template('armageddon/index.html')
    c = RequestContext(request, locals())
    return HttpResponse(t.render(c))

from armageddon.models import Vo_WallPoster
def api_handler_sendWallPoster(request):
    aSendWall = ct_armageddon.ct_sendWall(request)
    results = aSendWall.handleApiRequest()    
    templates = aSendWall.get_template()          
    c = RequestContext(request, locals())
    return HttpResponse(templates.render(c));
    
#    logging.info(1)
#    #logging.info(request.REQUEST.get('message'))
#    
#    #logging.info(unicode(request.GET['message']));
#       
#    review_ref = Vo_WallPoster(
#      uuid = util.get_universally_unique_identifiers(),          
#      name = request.GET['name'],          
#      message = request.GET['message'].decode('utf8')
#    )    
#    review_ref.put()
#    
#    t = loader.get_template('armageddon/index.html')
#    c = RequestContext(request, locals())
#    return HttpResponse(t.render(c))
    
def api_handler_getWallPoster(request):
    
    aGetWall = ct_armageddon.ct_getWall(request)
    results = aGetWall.handleApiRequest()    
    templates = aGetWall.get_template()          
    c = RequestContext(request, locals())
    return HttpResponse(templates.render(c))


    
    
    

