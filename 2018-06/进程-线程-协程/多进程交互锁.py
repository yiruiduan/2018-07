#!/usr/bin/python3
# -*- coding: utf-8 -*-
from multiprocessing import Lock,Process
import os

def f(l,i):
    l.acquire()
    try:
        print("hello ",i,os.getpid())
    finally:
        l.release()

if __name__=="__main__":
    lock=Lock()
    for num in range(10):
        p=Process(target=f,args=(lock,num))
        p.start()
