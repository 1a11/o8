import requests
import tools.userInfoHandler as uih
import tools.htmlHandler as hh
import modules.ok_checker as okc
import cloudscraper
import os
import uuid
import json

def makeAPIRequest(schema,p):
    urls=[]
    ids=[]
    data = {}
    scraper = cloudscraper.create_scraper()
    for i in schema:
        #print("Request type: {}".format(schema[i]['type']))
        #print("Request URL: {}".format(schema[i]['url']))
        permissions = uih.permissionsFor(i,p)
        info = uih.getUserDataWithPermissions(permissions,p)
        if schema[i]['type'] != 'local':
            try:
                request_url = schema[i]['url'].split('+')[0]
                #print(schema[i]['url'].split('+'))
                params = schema[i]['url'].split('+')[1]
                params = params.split('-')
                for i2 in params:
                    if i2 == 'ehash' or i2 == 'email':
                        for i3 in info[i2]:
                            urls.append(request_url.format(i3))
                            ids.append(i)
                    else:
                        urls.append(request_url.format(info[i2]))
                        ids.append(i)
            except Exception:
                pass
        else:
            if 'h8mail' in schema[i]['url']:
                permissions = uih.permissionsFor(i,p)
                info = uih.getUserDataWithPermissions(permissions,p)
                for i in info['email']:
                    command = 'h8mail -t {} > {}/data/{}h8mail.txt'.format(i,p,i)
                    os.system(command)
            elif 'okcheck' in schema[i]['url']:
                permissions = uih.permissionsFor(i,p)
                info = uih.getUserDataWithPermissions(permissions,p)

                phone_info = okc.find(info['phone'])
                email_info = {}
                for i in info['email']:
                    email_info[i] = okc.find(i)

                data['ok_info'] = {'phone_ok_info':phone_info,'email_ok_info':email_info}
            elif 'sherlock' in schema[i]['url']:
                permissions = uih.permissionsFor(i,p)
                info = uih.getUserDataWithPermissions(permissions,p)

                print(i)
                command = 'python3 {}sherlock {} -fo {}> {}/data/{}sherlock.txt'.format(p+'/tools/',' '.join(info['nickname']),p+'/data/sherlock/',p,str(uuid.uuid4()))
                print(command)
                os.system(command)
            elif 'phoneinfoga' in schema[i]['url']:
                permissions = uih.permissionsFor(i,p)
                info = uih.getUserDataWithPermissions(permissions,p)

                print(i)
                command = "Desktop/OSINT/tools/phoneinfoga scan -n {} > {}/data/{}phoneinfoga.txt".format(info['phone'],p,info['phone'])
                print(command)
                os.system(command)
    counter = 0
    print(urls)
    data['haveibeenpwned'] = []
    data['gravatar_name'] = []
    data['intelx']
    for i in urls:
        if 'intelx.io' not in i:
            print('[INFO] Checking',i)
            c = requests.get(i)
            if 'unifiedsearch' in i:
                cf_parsed = scraper.get(i).text
                if cf_parsed != '':
                    data['haveibeenpwned'].append('URL {}: Password breach'.format(i))
                else:
                    data['haveibeenpwned'].append('No haveibeenpwned breaches found for {}'.format(i))
            elif 'title' in c.text:
                #data['gravatar_name']=c.text
                print(ids[counter],p)
                data['gravatar_name'].append(hh.parseHTMLInfoFromPage(c.text,ids[counter],p))
            elif 'ip-api' in i:
                c = requests.get(i)
                data['ip'] = json.loads(c.text)
            else:
                #print('Need to parse HTML page')
                pass
            counter +=1
        else:
            data['intelx'].append('Check {} for IntelegenceX data.'.format(i))
    return data
