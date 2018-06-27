#!/usr/bin/python3
# -*- coding: utf-8 -*-

import gevent
import time
from gevent import monkey
from urllib.request import urlopen
monkey.patch_all()  #把当前程序的io操作单独的做上标记

def get_url(url):
    print("GET %s"%url)
    resp=urlopen(url)
    data=resp.read()
    print('%d bytes received from %s.' % (len(data), url))

urls=[
    "https://www.python.org/",
    "https://www.yahoo.com/",
    "https://github.com/"
]

start_time=time.time()
for url in urls:
    get_url(url)
print("\033[31;1m同步:%s\033[0m"%(time.time()-start_time))

async_start_time=time.time()
gevent.joinall([
    gevent.spawn(get_url,"https://www.python.org/"),
    gevent.spawn(get_url, "https://www.yahoo.com/"),
    gevent.spawn(get_url, "https://github.com/")
])
end_time=time.time()
print("\033[32;1m异步：%s\033[0m"%(end_time-async_start_time))