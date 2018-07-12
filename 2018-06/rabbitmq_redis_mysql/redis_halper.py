#!/usr/bin/python3
# -*- coding: utf-8 -*-
import redis
class RedisHelper(object):
    def __init__(self):
        self.connection=redis.Redis(host="192.168.1.161",port=8000,db=9)
        self.chan_sub="fm104.5"
        self.chan_pub = "fm104.5"

    def public(self, msg):
        self.connection.publish(self.chan_pub, msg)
        return True

    def subscribe(self):
        pub = self.connection.pubsub()   #打开收音机
        pub.subscribe(self.chan_sub)     #调频道
        pub.parse_response()             #准备接收
        return pub
