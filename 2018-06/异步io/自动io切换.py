#!/usr/bin/python3
# -*- coding: utf-8 -*-
import gevent
def fun():
    print("\033[31;1m初始化fun...1\033[0m")
    gevent.sleep(2)
    print("\033[31;1m初始化fun结束...5\033[0m")

def fun1():
    print("\033[32;1m初始化fun...2\033[0m")
    gevent.sleep(1)
    print("\033[32;1m初始化fun结束...4\033[0m")

def fun2():
    print("\033[33;1m初始化fun...3\033[0m")
    gevent.sleep(3)
    print("\033[33;1m初始化fun结束...6\033[0m")

gevent.joinall([
    gevent.spawn(fun),
    gevent.spawn(fun1),
    gevent.spawn(fun2)
])