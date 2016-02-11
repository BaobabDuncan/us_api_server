'''
Created on 2012. 2. 4.

@author: bond
'''

from kinggame import proxy

def getPenaltyList():
    return proxy.px_AdminPenalty().getPenaltyList()


def getTopPenaltyList(type='kr',next=None):    
    return proxy.px_AdminPenalty().getTopPenaltyList(type,next)

def getAdminPenaltyList(next=None):
    return proxy.px_AdminPenalty().getAdminPenaltyList(next)

def getAdminPenaltyById(id):
    return proxy.px_AdminPenalty().getAdminPenaltyById(id)

def updateDownloadCount(userPenaltyObject):
    userPenaltyObject.download_count = userPenaltyObject.download_count + 1
    userPenaltyObject.save()

def getUserPenaltyList():
    return proxy.px_UserPenalty().getUserPenaltyList()


def getUserPenaltyById(id):
    return proxy.px_UserPenalty().getUserPenaltyById(id)

def deleteUserPenalty(userPenaltyObject):
    userPenaltyObject.delete()