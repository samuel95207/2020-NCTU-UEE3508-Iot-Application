#!/usr/bin/env/ python3
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
LED_PIN = 12
GPIO.setup(LED_PIN,GPIO.OUT)

while(True):
    for i in range(3):
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(0.5)
    for i in range(3):
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(1)
    for i in range(3):
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(0.5)
    time.sleep(2)

GPIO.cleanup()
