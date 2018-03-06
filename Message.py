#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 15:58:57 2017

@author: abhilasha
"""

import urllib2
import json
phone = input("Enter receiver's number: ")
msg = input("Enter the message to send: ")
headers = { "X-Mashape-Authorization": "<Your API key at Mashape>" }
url = "https://160by2.p.mashape.com/index.php?msg="+msg+"&phone="+phone+"&pwd=your < password>&uid=<your user id>"
req = urllib2.Request(url, '', headers)
response = json.loads(urllib2.urlopen(req).read())
if response['response'] != "done\n":
    print ("Error")
else:
    print ("Message sent successfully")