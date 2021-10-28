#!/usr/bin/python3
# Get IPv4/6 geolocation and ownership data using ipgeolocation.io
# Requires ipgeolocation API key. Get yours at https://ipgeolocation.io/
# Usage: ./ip_scope.py <ipv4/6 address>

import sys
import requests
import ipaddress

# ipaddress module will validate the IPv4/6 address
IPADDR=ipaddress.ip_address(sys.argv[1])

# prompt for API Key
APIKEY=input('Please input your ipgeolocation.io API key and press enter: ')

# request ipgeolocation data
response = requests.get('https://api.ipgeolocation.io/ipgeo', params={'apiKey': APIKEY, 'ip': IPADDR, 'fields': 'organization,geo'})

# print ipgeolocation response data
print(response.content)
