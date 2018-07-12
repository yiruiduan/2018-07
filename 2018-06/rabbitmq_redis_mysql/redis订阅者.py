#!/usr/bin/python3
# -*- coding: utf-8 -*-
from redis_halper import RedisHelper
redis_helper=RedisHelper()
redis_sub = redis_helper.subscribe()
while True:
    msg = redis_sub.parse_response()
    print(msg)