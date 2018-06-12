#!/usr/bin/python3
# -*- coding: utf-8 -*-
import threading,time,queue

q = queue.Queue(maxsize=10)


def Porducer():
    count=1
    while True:
        q.put("骨头%s"%count)
        print("生产了骨头",count)
        count+=1
        time.sleep(2)

def Consumer(name):
    while True:
        print("[%s] 取到 %s并且吃了它"%(name,q.get()))
        time.sleep(1)

p=threading.Thread(target=Porducer)
p.start()
c=threading.Thread(target=Consumer,args=("wangcai",))
c.start()
c1=threading.Thread(target=Consumer,args=("xiaogou",))
c1.start()