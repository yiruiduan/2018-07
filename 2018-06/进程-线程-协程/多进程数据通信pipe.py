#!/usr/bin/python3
# -*- coding: utf-8 -*-
from multiprocessing import Process,Pipe
import time

def f(conn):
    conn.send([42, None, 'hello from child'])
    conn.send([42, None, 'hello from child1'])

    conn.close()

if __name__=="__main__":
    parent_conn,child_conn=Pipe()
    p=Process(target=f,args=(child_conn,))
    p.start()
    print(parent_conn.recv())
    print(parent_conn.recv())
    print(parent_conn.recv())

    p.join()