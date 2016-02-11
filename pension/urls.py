'''
Created on 2011. 7. 16.

@author: bond
'''
from django.conf.urls.defaults import patterns
urlpatterns = patterns('pension.handler_pension',     
    (r'^$', 'handler_front'),       
    (r'api/getNumber', 'api_handler_getNumber'),  
    (r'api/saveWallPoster', 'api_handler_saveWallPoster'), 
)
