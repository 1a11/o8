from colorama import init
from colorama import Fore, Back, Style

init()

def askForPersonInfo(schema):
    data = schema
    uinp = ' '
    for i in schema:
        if type(data[i]) != list:
            uinp = input("[INPUT] Input {} or press ENTER to skip ->   ".format(i))
            data[i] = uinp
        else:
            uinp = ' '
            print(Fore.YELLOW+'[WARNING] {} is a list, so you can put multiple values.'.format(i))
            while uinp != '':
                 uinp = input(Fore.GREEN+"[INPUT] Input {} or press ENTER to stop/skip ->   ".format(i))
                 if uinp != '':
                     data[i].append(uinp)
    return data
