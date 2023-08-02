#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
pir = 21
GPIO.setup(pir,GPIO.IN)
red = 17
green = 22
blue = 27
GPIO.setup(red,GPIO.OUT)
GPIO.setup(green,GPIO.OUT)
GPIO.setup(blue,GPIO.OUT)
GPIO.output(red,1)
GPIO.output(green,1)
GPIO.output(blue,1)
def rgb():
        GPIO.output(red,0)
        GPIO.output(green,1)
        GPIO.output(blue,1)
        time.sleep(0.5)
        GPIO.output(red,1)
        GPIO.output(green,0)
        GPIO.output(blue,1)
        time.sleep(0.5)
        GPIO.output(red,1)
        GPIO.output(green,1)
        GPIO.output(blue,0)
        time.sleep(0.5)
def cls():
        GPIO.output(red,1)
        GPIO.output(green,1)
        GPIO.output(blue,1)
try:
    while True:
        data = GPIO.input(pir)
        print("PIR 感測器:{0}".format(data))
        if data ==1 :
            rgb()
        else:
            cls()
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
