#!/usr/bin/python3
# -*- coding: utf-8 -*-
#运用线程的事件模式 events
import threading,time
import random
def light():
    count=0
    event.set()
    while True:
        if count>5 and count <=10:#改成红灯
            event.clear()
            print("\033[41;1m红灯\033[0m")
        elif count>10:#改成绿灯
            event.set()
            count=0
        else:
            print("\033[42;1m绿灯\033[0m")
        time.sleep(1)
        count+=1

def cars(name):
    while True:
        if event.is_set():
            print("[%s] running..."%name)
            time.sleep(1)
        else:
            print("[%s] waiting..."%name)
            event.wait()
            # print("[%s] start running..." % name)


event=threading.Event()

lights=threading.Thread(target=light)
lights.start()

car1=threading.Thread(target=cars,args=("test",))
car1.start()

