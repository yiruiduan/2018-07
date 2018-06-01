#!/usr/bin/python3
# -*- coding: utf-8 -*-
import threading,time
def run(n):
    print("running",n)
    time.sleep(2)

t1=threading.Thread(target=run,args=("t1",))
t2=threading.Thread(target=run,args=("t2",))
t1.start()
t2.start()