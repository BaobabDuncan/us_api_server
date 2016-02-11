'''
Created on 2011. 7. 16.

@author: bond
'''
from django.conf.urls.defaults import patterns
urlpatterns = patterns('kinggame.handler_kinggame',     
    (r'^$', 'handler_front'),     
    (r'adminpenaltylist', 'handler_adminpenaltylist'),
    
    
    
    (r'userpenaltylist/movieAdmin', 'handler_userpenaltymovieadmin'),
    (r'userpenaltylist/delete', 'handler_userpenaltydelete'),
    (r'userpenaltylist', 'handler_userpenaltylist'),    
    
    (r'penaltylist', 'handler_penaltylist'),
    
    (r'api/sendPenalty', 'api_handler_sendPenalty'),        
    (r'api/getPenalty', 'api_handler_getPenalty'),           
    (r'api/choicePenalty', 'api_handler_choicePenalty'),           
)
