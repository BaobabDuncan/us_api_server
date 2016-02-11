'''
Created on Apr 26, 2011

@author: woosanguk
'''
from django.template import RequestContext, loader
from django.http import HttpResponse,HttpResponseRedirect
from common import constants,user



def handler_Index(request):
    aAdminUser = user.adminUser()    
    if not aAdminUser.getAdminUser():
        return HttpResponseRedirect("/login/")        
        
    t = loader.get_template('index.html')
    c = RequestContext(request, locals())
    return HttpResponse(t.render(c));
    
def handler_Login(request):
    aAdminUser = user.adminUser()        
    if request.method == constants.RequestMethod['POST']:        
        if (constants.Admin_User['UserName'] == request.POST['username'] and constants.Admin_User['UserPass'] == request.POST['userpass']):
            aAdminUser.setAdminUser()
            return HttpResponseRedirect("/")             
    t = loader.get_template('login.html')
    c = RequestContext(request, locals())
    return HttpResponse(t.render(c));
