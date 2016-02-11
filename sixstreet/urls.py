'''
Created on May 11, 2011

@author: woosanguk
'''

from django.conf.urls.defaults import patterns
urlpatterns = patterns('sixstreet.handler_sixstreet',     
    (r'^$', 'handler_front'),
    (r'createClub', 'handler_createClub'),
    (r'createMember', 'handler_createMember'),
    (r'api/getClubList', 'api_handler_getClubList'),   
    (r'api/getClubMember', 'api_handler_getClubMember'),    
)

