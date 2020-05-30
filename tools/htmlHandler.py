from bs4 import BeautifulSoup
import tools.userInfoHandler as uih
import re

shit_list = ['Good news — no pwnage found!']

def parseHTMLInfoFromPage(code,id,p):
    soup = BeautifulSoup(code, 'lxml')
    element = uih.elementFor(id,p)
    fetched = ''
    if ':' in element:
        if element.split(':')[0] == 'class':
            fetched = soup.findAll("div", {"class": element.split(':')[1]})[0]#.select_one('h2').text
            print(fetched)
            if fetched in shit_list:
                fetched = 'No password leakage found on haveibeenpwned.'
    else:
        fetched = soup.select_one('title').text.split(' - ')[0]
        if fetched == 'Gravatar':
            fetched = "Gravatar name not registered."

    return fetched
