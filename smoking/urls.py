'''
Created on May 11, 2011

@author: woosanguk
'''

from django.conf.urls.defaults import patterns
urlpatterns = patterns('smoking.handler_smoking',     
    (r'^$', 'handler_front'),   
    (r'api/signUp', 'api_handler_signUp'),
    (r'api/sendMoney', 'api_handler_sendMoney'),
    (r'api/getTopRanking', 'api_handler_getTopRanking'),   
    (r'api/resetMoney', 'api_handler_resetMoney'),    
)

