#!/usr/bin/python3
# -*- coding: utf-8 -*-
#_*_coding:utf-8_*_
__author__ = 'Alex Li'
import threading
import time
import random

def door():
    count=0
    while True:
        if door_status_event.is_set():
            print("\033[42;1mdoor is opening...\033[0m")
            count+=1
        else:
            print("\033[41;1mdoor is closed...\033[0m")
            count=0
            door_status_event.wait()
        if count>3:
            print("\033[43;1mclose the door\033[0m")
            door_status_event.clear()
        time.sleep(0.5)


def staff(n):
    print("\033[32;1m[%s] is comming"%n)
    while True:
        if door_status_event.is_set():
            print("\033[32;1m[%s] is passing\033[0m"%n)
            break
        else:
            print("staff [%s] sees door got closed, swipping the card....." % n)
            door_status_event.set()

    time.sleep(1)

door_status_event=threading.Event()

door_status=threading.Thread(target=door)
door_status.start()
for i in range(10):
    people=threading.Thread(target=staff,args=(i,))
    time.sleep(random.randrange(3))
    people.start()