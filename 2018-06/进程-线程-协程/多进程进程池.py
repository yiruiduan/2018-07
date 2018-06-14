#!/usr/bin/python3
# -*- coding: utf-8 -*-
from multiprocessing import Process,Pool,freeze_support
import time,os
def Foo(i):
    time.sleep(2)
    print("in process:",os.getpid())
    return i+100

def Bar(arg):
    print("-->exec done",arg,os.getpid())

if __name__=="__main__":
    freeze_support()
    pool=Pool(5)
    print("主进程pid：",os.getpid())
    for i in range(10):
        # pool.apply_async(func=Foo,args=(i,))
        pool.apply_async(func=Foo,args=(i,),callback=Bar)

    print("end")
    pool.close()
    pool.join()#进程池中进程执行完毕后再关闭，如果注释，那么程序直接关闭。