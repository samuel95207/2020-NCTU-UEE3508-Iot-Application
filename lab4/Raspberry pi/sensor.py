#!/usr/bin/env/ python

import RPi.GPIO as GPIO
import time
import socket
import sys

GPIO.setwarnings(False)

HOST = '192.168.0.134'
PORT = 8001
sensor = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print 'socket created'

#v: speed of sound, TRIG: triger PIN, E: echo PIN
v = 343
TRIG = 16
E = 18

# LED PIN
LED_PIN = 12

# Set the modes of I/O
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN,GPIO.OUT)
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(E,GPIO.IN)
GPIO.output(TRIG,GPIO.LOW)

# A function that can calculate distance from Ultrasonic sensor echo pulse
def measure():
    #trigger the ultrasonic sensor by giving TRIG_PIN a single pulse
    GPIO.output(TRIG,GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIG,GPIO.LOW)

    pulse_start = 0
    pulse_end = 0
    #start timer when detecting falling edge
    while(GPIO.input(E) == GPIO.LOW):
        pulse_start = time.time()
    #stop timer when detecting rising edge
    while(GPIO.input(E) == GPIO.HIGH):
        pulse_end = time.time()

    #calculate the time sound wave had traveled
    t = pulse_end - pulse_start

    #calculate distance by the time sound wave had traveled
    d = t*v/2*100
    return d

while(True):
    #measure distance every loop and send data to server
    distance = measure()
    print(distance)
    time.sleep(0.5)

    # send data vbia UDP socket
    sensor.sendto(str(distance),('192.168.0.125',8001))

    if(10 < distance < 20):
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(0.1)
    elif(distance < 10):
        GPIO.output(LED_PIN, GPIO.HIGH)
    else:
        GPIO.output(LED_PIN, GPIO.LOW)

GPIO.cleanup()

