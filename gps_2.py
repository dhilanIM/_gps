import serial
#import RPi.GPIO as GPIO
import os, time
from decimal import *
delay = 1

FILE_NAME = "data.txt"
FILE_STAT = os.stat(FILE_NAME)  #Size of the file

#GPIO.setmode(GPIO.BOARD)
def find(str, ch):
    for i, ltr in enumerate(str):
        if ltr == ch:
            yield i
def saveData(lat,log)
    with open("data.txt","w") as d_file:
        d_file.write("Latitude: " + str(lat) + "Longitude: " + str(lon) + "\n")
        if file_stats >100000: #Delete data if exceeds 100 Kbytes
            d_file.truncate()

port = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=1)
cd=1
try:
    while cd <= 50:
        ck=0
        fd=''
    while ck <= 50:
        rcv = port.read(10)
        fd=fd+rcv
        ck=ck+1
    if '$GPRMC' in fd:
        ps=fd.find('$GPRMC')
        dif=len(fd)-ps
    if dif > 50:
        data=fd[ps:(ps+50)]
        print(data)
        p=list(find(data, ","))
        lat=data[(p[2]+1):p[3]]
        lon=data[(p[4]+1):p[5]]
        s1=lat[2:len(lat)]
        s1=Decimal(s1)
        s1=s1/60
        s11=int(lat[0:2])
        s1=s11+s1
        s2=lon[3:len(lon)]
        s2=Decimal(s2)
        s2=s2/60
        s22=int(lon[0:3])
        s2=s22+s2
        print("Latitude:",s1)
        print("Longitude:",s2)}
        saveData(s1,s2)
    cd=cd+1
    print(cd)
except KeyboardInterrupt:
    print("Thank You")
