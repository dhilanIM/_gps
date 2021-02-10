import time
import serial
import string
import pynmea2
import RPi.GPIO as gpio
import Adafruit_CharLCD as LCD #Adafruit Python Char LCD Library
gpio.setmode(gpio.BCM)
lcd = LCD.Adafruit_CharLCD(rs=26, en=19, d4=13, d5=6, d6=5, d7=11, cols=16, lines=2)
lcd.message("MSD Gurukul\n Welcomes You")
time.sleep(2)
lcd.clear()
lcd.message("GPS Demo")
time.sleep(2)
lcd.clear()

port = "/dev/ttyAMA0" # the serial port to which the pi is connected.

#create a serial object
ser = serial.Serial(port, baudrate = 9600, timeout = 0.5)
try:
    while 1:
        try:
            data = ser.readline()
        except:
            print("loading")  
        #wait for the serial port to churn out data

        if data[0:6] == '$GPGGA': # the long and lat data are always contained in the GPGGA string of the NMEA data
            msg = pynmea2.parse(data)
            latval = msg.lat #parse the latitude and print
            concatlat = "Lat:" + str(latval)
            print(concatlat)
            lcd.set_cursor(0,0)
            lcd.message(concatlat)

            #parse the longitude and print
            longval = msg.lon
            concatlong = "Long:"+ str(longval)
            print(concatlong)
            lcd.set_cursor(0,1)
            lcd.message(concatlong)
            time.sleep(0.5)#wait a little before picking the next data.
except KeyboardInterrupt:
    lcd.clear()
    lcd.message("Thank You")
    time.sleep(2)