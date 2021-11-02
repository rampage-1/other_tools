#!/usr/bin/env python3
# Fetch a url. Usage: ./url-fetch.py <URL>
# Study of HTTP GET requests and their attributes, using requests library
import requests
import sys

# trim trailing / from url
URL=sys.argv[1].rstrip("/")
ENDPOINT='/directory'

PARAMETERS={'key[value]':'1'}
COOKIES=dict(cookie='a1b2c3d4')
HEADERS={'Content-Type':'key/value','Accept-Language':'*','X-HTTP-Method-Override':'CUSTOM','X-Forwarded-For':'10.0.2.21','X-Forwarded-Host':'targetdomain11.com'}

response = requests.get(URL+ENDPOINT, params=PARAMETERS, cookies=COOKIES, headers=HEADERS)

# special case (sc): send duplicate parameters
# ex: http://subdom.dom.tld/directory?key=value&key=value
# sc = requests.post(URL+ENDPOINT, params=[('key','value'),('key','value')], cookies=COOKIES, headers=HEADERS)

# special case (sc): append null byte to prepared request url 
#sc = requests.get(response.request.url+'%00')

# special case (sc): append double encoded null byte to request url
# %00 double encoded is %2500 (% encoded is %25)
#sc = requests.get(URL+ENDPOINT, params={'key':'value%00'}, cookies=COOKIES, headers=HEADERS)

# special case (sc): custom method
#sc = requests.request('CUSTOM', URL+ENDPOINT)

# special case (sc): path-as-is; requests is trimming an attempt at fragmentation.
# Append fragment (#, /../, etc...) to url
PATH = URL+ENDPOINT+'#directory'
s = requests.Session()
r = requests.Request(method='GET', url=PATH)
prep = r.prepare()
prep.url = PATH
sc = s.send(prep)

# review request
print('\n')
print('----- request attributes -----')
print('Request URL: ' + str(response.request.url))
print('Headers: ' + str(response.request.headers))
print('Hooks: ' + str(response.request.hooks))
print('Body: ' + str(response.request.body))
print('\n')

# output response
print('----- response attributes ----')
print('Response URL: ' + str(response.url))
print('Content: \n' + str(response.content))
print('\n')

print('----- special request -----')
print('Response URL: \n' + str(sc.url))
print('Content: \n' + str(sc.content))
