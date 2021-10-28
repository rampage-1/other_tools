#!/bin/bash
# Get IPv4/6 geolocation and ownership data using ipgeolocation.io
# Requires ipgeolocation API key. Get yours at https://ipgeolocation.io/
# Usage: ./ip_scope.sh <ipv4/6 address>

ipaddr=$1

# validate IP address (https://www.linuxjournal.com/content/validating-ip-address-bash-script)
function valid_ip()
{
    local stat=1

    if [[ $ipaddr =~ ^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$ ]]; 
        then
        OIFS=$IFS
        IFS='.'
        ip=($ipaddr)
        IFS=$OIFS
        [[ ${ip[0]} -le 255 && ${ip[1]} -le 255 && ${ip[2]} -le 255 && ${ip[3]} -le 255 ]]
    stat=$?
    
    # IPv6 validation (https://stackoverflow.com/questions/53497)  
    elif [[ $ipaddr =~ ^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))$ ]]; 
	    then 
	    stat=$?
    fi
    return $stat
}

if valid_ip $ip;
    then 
    # prompt for API key to keep it out of bash_history
    echo "Please enter ipgeolocation.io API key and press enter " && read apikey
    curl 'https://api.ipgeolocation.io/ipgeo?apiKey='$apikey'&ip='$ipaddr'&fields=organization,geo';

else
    echo "Invalid IPv4 or IPv6 Address";
fi
