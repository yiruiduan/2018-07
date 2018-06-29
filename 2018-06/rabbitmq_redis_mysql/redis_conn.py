#!/usr/bin/python3
# -*- coding: utf-8 -*-
from rediscluster import StrictRedisCluster
import sys
def redis_cluster():
    redis_nodes=[{"host":"192.168.1.161","port":7000},
                 {"host": "192.168.1.161", "port": 7001},
                 {"host": "192.168.1.161", "port": 7002},
                 {"host": "192.168.1.147", "port": 7000},
                 {"host": "192.168.1.147", "port": 7001},
                 {"host": "192.168.1.147", "port": 7002}]
    try:
        redisconn=StrictRedisCluster(startup_nodes=redis_nodes)
    except Exception as e:
        print("connect error!!")
        sys.exit(1)
    redisconn.set("ni","hao")
    print(redisconn.get("ni"))
redis_cluster()