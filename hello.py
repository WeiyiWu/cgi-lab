#!/usr/bin/env python3
import os, json, cgi
from templates import *
from secret import *
print("Content-type: text/html\r\n\r\n")
print("<title>Test CGI</title>")
print("<p>Hello World CMPUT404!</p>")


#Question 1
# print(os.environ)
json_object = json.dumps(dict(os.environ), indent = 4)
# print(json_object)

# Question 2
for param in os.environ.keys():
    if (param=="QUERY_STRING"):
        print("<b>%20s</b>: %s<br>" % (param, os.environ[param]))

#Question 3
for param in os.environ.keys():
    if (param=="HTTP_USER_AGENT"):
        print("<b>%20s</b>: %s<br>" % (param, os.environ[param]))

if len(os.environ['HTTP_COOKIE'])==0:
    print(login_page())

else:
    cookie_data = os.environ['HTTP_COOKIE'].split('; ')
    cookie_dict = {i.split('=')[0]:i.split('=')[1] for i in cookie_data}
    if ('UserID' not in cookie_dict.keys()) or ('Password' not in cookie_dict.keys()):
        print(login_page())
        
    elif cookie_dict['UserID']==username and cookie_dict['Password']==password:
        print(secret_page(cookie_dict['UserID'], cookie_dict['Password']))

    else:
        print(login_page())
        