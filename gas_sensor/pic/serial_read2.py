#!/usr/bin/env python
#This is working good
import time
import serial
y = 'c'          
ser = serial.Serial(          
    port='/dev/ttyAMA0',
    baudrate = 9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
    )
counter=0
ser.write (y.encode())
while 1:
    #serialcmd = input("c serial command: ")
    
    x=ser.readline()
    print (x)
    #time.sleep(1)
    counter += 1
    