#!/usr/bin/python3
# -*- coding: utf-8 -*-
import redis,time
pool=redis.ConnectionPool(host="192.168.1.161",port=8000,db=5)

r=redis.Redis(connection_pool=pool)
pipe=r.pipeline(transaction=True)

pipe.set("name","zhangye")

time.sleep(50)
pipe.set("role","haoren")
# r.brpoplpush("names","names7",timeout=50)
# r.set("name7","nihao ")
pipe.execute()