#!/usr/bin/env python3
# Created for study of HTTP requests and their various attributes
# Post to a url. Usage: ./url-post.py <URL>
import requests
import sys

# trim trailing / from url
URL=sys.argv[1].rstrip("/")
ENDPOINT='/directory'

PARAMETERS={'key':'value'}

# cookies and headers
COOKIES=dict(cookie='efa43b02f')
HEADERS={'Content-Type':'application/yaml','Accept-Language':'en-US,en;q=0.5'}

# data
BODY={'key':'value'}
#XML=b'<key><value><value></value></key>'
# using HTML character entities
XML="""<key><value>&amp;value</value></key>"""
JSON={'key': 'value\"'}
YAML={'key':'value'}

# post multipart encoded file
FILE = {'filename': ('../../dummy.txt', open('dummy.txt'))}

# general send post request.
response = requests.post(URL+ENDPOINT, headers=HEADERS, json=YAML, file=FILE)

# special case (sc): send json (set 'Content-Type':'application/json')
#response = requests.post(URL+ENDPOINT, headers=HEADERS, json=JSON)

# special case (sc): send yaml (because yaml is a superset of json)
#response = requests.post(URL+ENDPOINT, headers=HEADERS, json=YAML)

# special case (sc): send duplicate data values
#response = requests.post(URL+ENDPOINT, data=[('key','value'),('key','value')])

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
print('Response Code: ' + str(response.status_code))
print('Content: \n' + str(response.content))
print('\n')
