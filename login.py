#!/usr/bin/env python3
import os, json, cgi
from secret import *
from templates import *

form = cgi.FieldStorage() 
get_username = form.getvalue("username")
get_password = form.getvalue("password")

if get_username == username and get_password == password:
    print("Set-Cookie: UserID = %s" % get_username)
    print("Set-Cookie: Password = %s" % get_password)
    print("Cookie: UserID = %s; Password = %s" % (get_username, get_password))
    print("Content-type: text/html\r\n\r\n")
    print("<b>%20s</b>: %s<br>" % ('HTTP_COOKIE', os.environ['HTTP_COOKIE']))
    print(secret_page(get_username, get_password))

else:
    print("Content-type: text/html\r\n\r\n")
    print(after_login_incorrect())
    print(login_page())
