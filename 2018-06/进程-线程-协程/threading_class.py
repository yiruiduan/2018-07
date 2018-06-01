#!/usr/bin/python3
# -*- coding: utf-8 -*-

import threading,time
class MyThread(threading.Thread):
    def __init__(self,n):
        super(MyThread,self).__init__()
        self.n=n

    def run(self):
        print("running ",self.n)
        time.sleep(2)

thread_list=[]
start_time=time.time()
for i in range(50):
    t=MyThread(i)
    thread_list.append(t)
    t.start()

for res in thread_list:
    res.join()
end_time=time.time()
print(end_time-start_time)