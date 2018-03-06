#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 14:41:13 2017          

@author: abhilasha
"""
#N=10
import serial
from twilio.rest import Client
ser=serial.Serial('/dev/ttyACM1', 9600)
sensor1=[]
sensor2=[]
account_sid="abcd"
auth_token="abcd"
twilioclient=Client(account_sid, auth_token)
def sendMessage(myTwilioNumber,destCellPhone,message):
    twilioclient.messages.create(to=destCellPhone,from_=myTwilioNumber,body=message)

for i in range(0,3):
    data=ser.readline().rstrip()
    pro_data=float(data)
    if(i%2!=0):
        sensor1.append(pro_data)
        if pro_data>1.50:
            sendMessage("NumTwiliogives","YourNum","Valve 1 is on")
        else:
            sendMessage("NumTwiliogives","YourNum","Valve 1 is off")
    else:
        sensor1.append(pro_data)
        if pro_data>1.50:
            sendMessage("NumTwiliogives","YourNum","Valve 2 is on")
        else:
            sendMessage("NumTwiliogives","YourNum","Valve 2 is off")
        
        
    
    

    



    
