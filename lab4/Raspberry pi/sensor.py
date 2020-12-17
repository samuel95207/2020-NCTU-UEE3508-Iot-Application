#!/usr/bin/env/ python3

import RPi.GPIO as GPIO
import time
import socket
import sys

GPIO.setwarnings(False)

HOST = '192.168.0.134'
PORT = 8001
sensor = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print 'socket created'

v = 343
TRIG = 16
E = 18

LED_PIN = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN,GPIO.OUT)
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(E,GPIO.IN)
GPIO.output(TRIG,GPIO.LOW)

def measure():
    GPIO.output(TRIG,GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIG,GPIO.LOW)
    pulse_start = 0
    pulse_end = 0
    while(GPIO.input(E) == GPIO.LOW):
        pulse_start = time.time()
    while(GPIO.input(E) == GPIO.HIGH):
        pulse_end = time.time()

    t = pulse_end - pulse_start

    d = t*v/2*100
    return d

while(True):
    distance = measure()
    print(distance)
    time.sleep(0.5)
    if(10 < distance < 20):
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(0.1)
        sensor.sendto(str(distance),('192.168.0.125',8001))
    elif(distance < 10):
        GPIO.output(LED_PIN, GPIO.HIGH)
        sensor.sendto(str(distance),('192.168.0.125',8001))
    else:
        GPIO.output(LED_PIN, GPIO.LOW)
        sensor.sendto(str(distance),('192.168.0.125',8001))

GPIO.cleanup()

