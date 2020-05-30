import json
import os
import glob
import tools.userInfoHandler as uih


codeblocks ={'first name':"""<p>First name: {} <br></p>""",
             'middle name':"""<p>Middle name: {} <br></p>""",
             'last name':"""<p>Last name: {} <br></p>""",
             'phone':"""<p>Phone number: {} <br></p>""",
             'namelist':"""<p>Name list: {} <br></p>""",
             'country':"""<p>Country: {} <br></p>""",
             'address':"""<p>Address: {} <br></p>""",
             'email':"""<p><p>Email addresses:<br><hr color="#000" /> {} <hr color="#000" /></p>""",
             'nickname':"""<p>Sherlock usernames report:</p><hr color="#000" /><p> {} </p><hr color="#000" /><p> {} </p><hr color="#000" />""",
             'gravatar_name':"""<p>Gravatar name(s): {} <br></p>""",
             'ip':"""<p>IP-lookup:<br> <hr color="#000" />{}<hr color="#000" /></p>""",
             'haveibeenpwned':"""<p>Leaked: {} <br></p>""",
             'intelx':"""<p>IntelX links: {} <br></p>""",
             'h8mail':"""<p>H8mail password leak:</p><hr color="#000" /><p>{}</p><hr color="#000" />""",
             'phoneinfoga':"""<p>Phoneinfoga info:</p><hr color="#000" /><p>{}</p><hr color="#000" />""",
             'ok_info':"""<p>OK.ru (Russian bs):</p><hr color="#000" /><p>{}</p><hr color="#000" />"""}

def parseDataToReadable(data,p):
    h8log = []
    shlog = []
    shslog = []
    phoneinfoga = ''
    print(glob.glob(p+'/data/*h8mail.txt'))
    for filename in glob.glob(p+'/data/*h8mail.txt'):
        print('Reading file {}'.format(filename))
        f = open(filename,'r')
        h8log.append(f.read())
        f.close()
    for filename in glob.glob(p+'/data/*sherlock.txt'):
        print('Reading file {}'.format(filename))
        f = open(filename,'r')
        shlog.append(f.read())
        f.close()
    for filename in glob.glob(p+'/data/sherlock/*.txt'):
        print('Reading file {}'.format(filename))
        f = open(filename,'r')
        shslog.append(f.read())
        f.close()
    for filename in glob.glob(p+'/data/*phoneinfoga.txt'):
        print('Reading file {}'.format(filename))
        f = open(filename,'r')
        phoneinfoga = f.read()
        f.close()
    with open(p+'/data/personSchema.json', "r", encoding='utf8') as read_file:
        info = json.load(read_file)
    #14

    print(h8log,shlog,shslog,phoneinfoga)

    f = open(p+'/tools/report_template.html','r')
    code = f.read()
    f.close()
    try:
        code+=codeblocks['first name'].format(info['first name'])
    except Exception:
        pass
    try:
        code+=codeblocks['middle name'].format(info['middle name'])
    except Exception:
        pass
    try:
        code+=codeblocks['last name'].format(info['last name'])
    except Exception:
        pass
    try:
        code+=codeblocks['phone'].format(info['phone'])
    except Exception:
        pass
    try:
        code+=codeblocks['namelist'].format('\n'.join(info['namelist']))
    except Exception:
        pass
    try:
        code+=codeblocks['address'].format(info['address'])
    except Exception:
        pass
    try:
        code+=codeblocks['email'].format('\n'.join(info['email']))
    except Exception:
        pass
    try:
        code+=codeblocks['nickname'].format('\n-*-*-*-*-*-*-*-*-*-*-*-*-*-*'.join(shlog),'\n-*-*-*-*-*-*-*-*-*-*-*-*-*-*'.join(shslog))
    except Exception:
        pass
    try:
        code+=codeblocks['gravatar_name'].format('\n'.join(data['gravatar_name']))
    except Exception:
        pass
    try:
        code+=codeblocks['ip'].format(data['ip'])
    except Exception:
        pass
    try:
        code+=codeblocks['haveibeenpwned'].format('\n'.join(data['haveibeenpwned']))
    except Exception:
        pass
    try:
        code+=codeblocks['intelx'].format('\n'.join(data['intelx']))
    except Exception:
        pass
    try:
        code+=codeblocks['h8mail'].format('\n-*-*-*-*-*-*-*-*-*-*-*-*-*-*'.join(h8log))
    except Exception:
        pass
    try:
        code+=codeblocks['phoneinfoga'].format(phoneinfoga)
    except Exception:
        pass
    try:
        code+=codeblocks['ok_info'].format(data['ok_info'])
    except Exception:
        pass


    code+="""</body></html>"""
    print(code)
    f = open(p+'/report.html','w')
    f.write(code)
    f.close()
    f = open(p+'/report.html','r')
    code = ''
    hend = False
    for i in f:
        if hend:
            code+=i+'<br>'
        if '</head>' in i:
            hend = True
    f.close()
    f = open(p+'/report.html','w')
    f.write(code)
    f.close()
