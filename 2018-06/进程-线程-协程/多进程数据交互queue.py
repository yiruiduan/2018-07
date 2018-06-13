#!/usr/bin/python3
# -*- coding: utf-8 -*-
#父进程在创建子进程时候克隆了一个q给子进程
from multiprocessing import Process,Queue
def f(q):
    q.put([42,None,"hello"])

if __name__=="__main__":
    q=Queue()
    p=Process(target=f,args=(q,))
    p.start()
    print(q.get())