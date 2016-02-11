# -*- encoding:utf-8 -*-
'''
Created on May 11, 2011

@author: woosanguk
'''

from django.conf.urls.defaults import patterns
urlpatterns = patterns('elecboard.handler_elecboard',     
    (r'^$', 'handler_front'),       
    (r'api/getWallPoster', 'api_handler_getWallPoster'),   
    (r'api/sendWallPoster', 'api_handler_sendWallPoster'),    
)

