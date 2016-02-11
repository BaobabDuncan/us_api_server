'''
Created on Apr 26, 2011

@author: woosanguk
'''
from django.conf.urls.defaults import patterns,include

urlpatterns = patterns('',  
)

# index page
urlpatterns += patterns('viewIndex.handler_Index',
    (r'^$','handler_Index'),
    (r'login','handler_Login'),
)

# smoking server
urlpatterns += patterns('smoking.handler_smoking',
    (r'smoking/',include('smoking.urls')),
)

# armageddon server
urlpatterns += patterns('armageddon.handler_armageddon',
    (r'armageddon/',include('armageddon.urls')),
)

# sixstreet server
urlpatterns += patterns('sixstreet.handler_sixstreet',
    (r'sixstreet/',include('sixstreet.urls')),
)

# pension server
urlpatterns += patterns('pension.handler_pension',
    (r'pension/',include('pension.urls')),
)

# elec board
urlpatterns += patterns('elecboard.handler_elecboard',
    (r'elecboard/',include('elecboard.urls')),
)

# king game
urlpatterns += patterns('kinggame.handler_kinggame',
    (r'kinggame/',include('kinggame.urls')),
)
