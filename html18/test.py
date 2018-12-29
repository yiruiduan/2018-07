#!/usr/bin/python3
# -*- coding: utf-8 -*-
from rediscluster import StrictRedisCluster
import sys
import redis

def redis_cluster():

    try:
        # redisconn=StrictRedisCluster(startup_nodes=redis_nodes)
        pool = redis.ConnectionPool(host='192.168.1.129', port=6379,password='Ccicoiroad123456')
    except Exception as e:
        print("connect error!!")
        sys.exit(1)
    # redisconn.hset("info1","name","yiruiduan")
    # redisconn.hset("info1","age",30)
    # redisconn.hset("info1","id",2)
    r = redis.Redis(connection_pool=pool);
    # redisconn.hset("info1","name","yiruiduan")
    # redisconn.hset("info1","age",30)
    r.hset("info1","id",2)
    # for key in redisconn.keys():
    #     redisconn.delete(key)
    print(type(r.hgetall("info1")))
redis_cluster()