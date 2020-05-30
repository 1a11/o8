import requests
import json
import random
import uuid
import info.parser as parser
import tools.formatter as formatter
import modules.decoder as decoder
import tools.requester as rq
import tools.reportCreator as rc
from colorama import init
from colorama import Fore, Back, Style
import os, sys
init()

print(Fore.GREEN+'O8 OSINT Tool\n')
print("Let's find some shit!")
print('---------------------')
schema = {'first name':'',
          'middle name':'',
          'last name':'',
          'email':[],
          'nickname':[],
          'phone':'',
          'ip':'',
          'country':'',
          'address':''}

data = parser.askForPersonInfo(schema)
if data['first name'] != '' and data['middle name'] != '' and data['last name'] != '':
    data['namelist'] = formatter.getNameVariations(data['first name'],data['middle name'],data['last name'])
else:
    data['namelist'] = []
p = os.path.dirname(os.path.abspath(__file__))
with open(p+'/data/config.json', "r", encoding='utf8') as read_file:
    config = json.load(read_file)

print("\n\nGreat. Let's choose bases to check against.")
print("[HELP] Print 99 to chose all.")
print('[HELP] Print numbers, separated with "," to chose multiple databases.')
print("---------------------------------------------")
for i in config:
    print("{}|{}".format(i,config[i]['description']))
print("---------------------------------------------")
uinp = input('-> ')

c_databases = []

if uinp == '99':
    for i in range(len(config)):
        c_databases.append(str(i))
else:
    c_databases = uinp.split(',')
    for i in c_databases:
        try:
            int(i)
        except Exception:
                print(Fore.RED+'[ERROR] Params list incorrect.')
                sys.exit()
print('Choosen: {}'.format(str(c_databases).strip('[]').replace("'",'')))
print('Setting up model file for user data handler...')
with open(p+'/data/personSchema.json', "w", encoding='utf8') as out_file:
    data = json.dump(schema, out_file, indent=4)
print('Done.')
print('Starting OSINT procedure...')
data = decoder.translateIdsToModulesNames(c_databases,p)
data = rq.makeAPIRequest(data,p)
print('Done.')
print('Creating report...')
print(data)
rc.parseDataToReadable(data,p)
