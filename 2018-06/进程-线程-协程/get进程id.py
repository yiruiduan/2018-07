#!/usr/bin/python3
# -*- coding: utf-8 -*-

from multiprocessing import Process
import os


def info(title):
    print(title)
    print("module_name:",__name__)
    print("parent_id:",os.getppid())
    print("process_id:",os.getpid())
    print("\n")
def f(name):
    info("\033[31;1min function f\033[0m")
    print("hello",name)

if __name__=="__main__":
    info("\033[32;1mmain process line\033[0m")
    p=Process(target=f,args=("yinuo",))
    p.start()