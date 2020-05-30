#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup

OK_LOGIN_URL = \
    'https://www.ok.ru/dk?st.cmd=anonymMain&st.accRecovery=on&st.error=errors.password.wrong'
OK_RECOVER_URL = \
    'https://www.ok.ru/dk?st.cmd=anonymRecoveryAfterFailedLogin&st._aid=LeftColumn_Login_ForgotPassword'


def check_login(login_data):
    session = requests.Session()
    session.get(f'{OK_LOGIN_URL}&st.email={login_data}')
    request = session.get(OK_RECOVER_URL)
    root_soup = BeautifulSoup(request.content, 'html.parser')
    soup = root_soup.find('div', {'data-l': 'registrationContainer,offer_contact_rest'})
    if soup:
        account_info = soup.find('div', {'class': 'ext-registration_tx taCenter'})
        masked_email = soup.find('a', {'data-l': 't,email'})
        masked_phone = soup.find('a', {'data-l': 't,phone'})
        if masked_phone:
            masked_phone = masked_phone.get('data-post')
        if masked_email:
            masked_email = masked_email.get('data-post')
        if account_info:
            masked_name = account_info.find('div', {'class': 'ext-registration_username_header'})
            if masked_name:
                masked_name = masked_name.get_text()
            account_info = account_info.findAll('div', {'class': 'lstp-t'})
            if account_info:
                profile_info = account_info[0].get_text()
                profile_registred = account_info[1].get_text()
            else:
                profile_info = None
                profile_registred = None
        else:
            return None

        return {
            'masked_name': masked_name,
            'masked_email': masked_email,
            'masked_phone': masked_phone,
            'profile_info': profile_info,
            'profile_registred': profile_registred,
        }

    if root_soup.find('div', {'data-l': 'registrationContainer,home_rest'}):
        return 'not associated'


def console_output(login_data, parsed_response):
    if parsed_response:
        if parsed_response == 'not associated':
            print(f'{login_data} not associated with ok.ru login')
            return(f'{login_data} not associated with ok.ru login')
        else:
            print(f'{login_data} associated with ok.ru login')
            return parsed_response.items()

    else:
        print('No fault, but server return unknown response')


def find(args):
    response = check_login(args)
    return(response)
