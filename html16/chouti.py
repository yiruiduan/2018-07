#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests

i1 = requests.get(url= "https://dig.chouti.com/all/hot/recent/1")
print(i1)
print(i1.cookies.get_dict())

i2 = requests.post(
    url= "https://dig.chouti.com/login",
    data= {
        'phone': "8613321123557",
        'password': "530487",
        'oneMonth': ""
    },
    cookies = i1.cookies.get_dict()
)
print(i2)