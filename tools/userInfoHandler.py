import json, os
import hashlib

def permissionsFor(id,p):
    with open(p+'/data/modulesMap.json', "r", encoding='utf8') as read_file:
        config = json.load(read_file)
    return config[id]['params']

def getUserDataWithPermissions(permissions,p):
    with open(p+'/data/personSchema.json', "r", encoding='utf8') as read_file:
        config = json.load(read_file)
    fetched = {}
    for i in permissions:
        if i != 'ehash':
            fetched[i] = config[i]
        elif i == 'ehash':
            tohash = config['email']
            hashed = []
            for i2 in tohash:
                hashed.append(hashlib.md5(i2.encode()).hexdigest())
            fetched[i] = hashed
    return fetched

def elementFor(id,p):
    with open(p+'/data/modulesMap.json', "r", encoding='utf8') as read_file:
        config = json.load(read_file)
    return config[id]['element']
