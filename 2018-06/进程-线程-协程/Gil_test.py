#!/usr/bin/python3
# -*- coding: utf-8 -*-

import threading,time
def run(n):
    lock.acquire()
    global num
    time.sleep(0.1)
    num-=1
    lock.release()

num=100
lock=threading.Lock()
t_obj=[]
for i in range(100):
    t=threading.Thread(target=run,args=(i,))
    t_obj.append(t)
    t.start()

for t in t_obj:
    t.join()

print("______all threads has finished....",threading.current_thread())
print("num:",num)