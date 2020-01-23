#!/usr/bin/env python3
import cgi
import os
import cgitb
cgitb.enable()

print('Content-Type: text/html\n')
print()
print('<!doctype html><title>Hello</title><h2>Hello World</h2>')

#Q1
#print(os.environ)

#Q2
print(os.environ["QUERY_STRING"])

#Q3
#print(os.environ["HTTP_USER_AGENT"])
