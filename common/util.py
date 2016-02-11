'''
Created on Feb 15, 2011

@author: woosanguk
'''

import uuid
def get_universally_unique_identifiers():
    _generate_uuid = str(uuid.uuid4().hex)      
    return charShowWhereIsNumber(_generate_uuid,30)

def charShowWhereIsNumber(str,num):
    return str[:int(num)]

from datetime import datetime
def getRegdate():
    return datetime.now()

    

    